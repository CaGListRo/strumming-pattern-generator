from button import Button
from slot_indicator import SlotIndicator
from check_box import CheckBox

import pygame as pg

from random import choice
from typing import Final
from time import perf_counter

class StrummingPatternGenerator:
    FPS: Final[int] = 30

    def __init__(self) -> None:
        """ Initializes the Strumming Pattern Generator app. """
        pg.init()
        self.screen: pg.display = pg.display.set_mode((475, 300))
        pg.display.set_caption("Strumming Pattern Generator")
        icon = pg.image.load("icon.png").convert_alpha()
        icon_surf = pg.surface.Surface((32, 32))
        icon_surf.blit(icon, (0, 0))
        pg.display.set_icon(icon)
        self.font: pg.font.Font = pg.font.SysFont("comicsans", 23)

        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
        self.generate: bool = False
        # buttons
        self.generate_button: Button = Button(mid_pos=(302, 25), size=(150,32), name="(Re)Generate",color_schema="green")
        self.plus_one_button: Button = Button(mid_pos=(155, 25), size=(32,32), name="+1",color_schema="white")
        self.plus_ten_button: Button = Button(mid_pos=(191, 25), size=(32,32), name="+10",color_schema="yellow")
        self.minus_one_button: Button = Button(mid_pos=(61, 25), size=(32,32), name="-1",color_schema="white")
        self.minus_ten_button: Button = Button(mid_pos=(25, 25), size=(32,32), name="-10",color_schema="yellow")
        self.play_button: Button = Button(mid_pos=(450, 25), size=(32,32), name="|>",color_schema="green")
        self.stop_button: Button = Button(mid_pos=(414, 25), size=(32,32), name="[]",color_schema="red")
        self.buttons: list[Button] = [self.generate_button, self.plus_one_button, self.plus_ten_button,
                                     self.minus_one_button, self.minus_ten_button, self.play_button,
                                     self.stop_button]

        # load images
        self.arrow_down: pg.Surface = pg.image.load("arrow.png").convert_alpha()
        self.arrow_up: pg.Surface = pg.image.load("arrow.png").convert_alpha()
        self.arrow_up = pg.transform.rotate(self.arrow_up, 180)
        self.background: pg.Surface = pg.image.load("background.png")
        chkbox_0: pg.Surface = pg.image.load("check_box_0.png").convert_alpha()
        chkbox_1: pg.Surface = pg.image.load("check_box_1.png").convert_alpha()

        self.sound_check_box: CheckBox = CheckBox(font=self.font, text="Sound", mid_pos=(25, 275), images=[chkbox_1, chkbox_0], active=True)
        self.strum_check_box: CheckBox = CheckBox(font=self.font, text="Strum", mid_pos=(150, 275), images=[chkbox_1, chkbox_0], active=False)
        self.forth_check_box: CheckBox = CheckBox(font=self.font, text="4/4", mid_pos=(275, 275), images=[chkbox_1, chkbox_0], active=True)
        
        # slot indicators
        self.si_states: list[bool] = [True, False, False, False, False, False, False, False]
        self.slot_indicators: list[SlotIndicator] = []
        for i in range(8):
            self.slot_indicators.append(SlotIndicator(pos=(14 + i * 60, 50)))
            self.slot_indicators[i].set_state(self.si_states[i])
        self.current_slot: int = 0

        self.arrows: list[bool] = []
        self.bpm: int = 120        
        self.timer: float = 0.0
        self.play: bool = False
        self.play_forth: bool = True
        self.play_strum: bool = False

        # sound
        pg.mixer.init()
        pg.mixer.set_num_channels(20)
        self.sound_enabled: bool = True
        self.sound_1: pg.mixer.Sound = pg.mixer.Sound("metronom click 1.wav")
        self.sound_2: pg.mixer.Sound = pg.mixer.Sound("metronom click 2.wav")

    def event_handler(self) -> None:
        """ Handles events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def check_elements(self) -> None:
        """ Checks if the generate_button is clicked. """
        self.generate = self.generate_button.check_collision()
        if self.generate:
            self.generate_arrows()
        if self.plus_one_button.check_collision():
            self.bpm += 1 if self.bpm < 300 else self.bpm
        if self.plus_ten_button.check_collision():
            self.bpm += 10 if self.bpm < 290 else self.bpm
        if self.minus_one_button.check_collision():
            self.bpm -= 1 if self.bpm > 1 else self.bpm
        if self.minus_ten_button.check_collision():
            self.bpm -= 10 if self.bpm > 10 else self.bpm
        if self.play_button.check_collision():
            self.play = True
        if self.stop_button.check_collision():
            self.play = False

        if self.sound_check_box.check_collision():
            self.sound_enabled = True if self.sound_check_box.get_state() else False
        if self.forth_check_box.check_collision():
            self.play_forth = True if self.forth_check_box.get_state() else False
            self.strum_check_box.set_state(False if self.play_forth else True)
            self.play_strum = False
        if self.strum_check_box.check_collision():
            self.play_strum = True if self.strum_check_box.get_state() else False
            self.forth_check_box.set_state(False if self.play_strum else True)
            self.play_forth = False

    def generate_arrows(self) -> None:
        """ Generates arrows on the screen. """
        self.arrows = [choice((True, False)) for _ in range(8)]
        self.generate = False

    def draw_arrows(self, idx: int) -> None:
        if self.arrows[idx]:
            if idx % 2 == 0:
                self.screen.blit(self.arrow_down, (idx * 60, 70))
            else:
                self.screen.blit(self.arrow_up, (idx * 60, 70))

    def play_sound(self, slot: int) -> None:
        """
        Plays a sound based on the slot.
        Args:
        slot (int): The slot to play the sound for.
        """
        if self.play_forth:
            if slot == 0:
                self.sound_2.play()
            elif slot % 2 == 0:
                self.sound_1.play()
        elif self.play_strum and len(self.arrows) > 0:
            if self.arrows[slot]:
                if slot % 2 == 0:
                    self.sound_2.play()
                else:
                    self.sound_1.play()

    def update_slot_indicator(self, dt: float) -> None:
        """ Updates the slot indicators. """
        beat_time: float = 60 / (self.bpm * 4)
        self.timer += dt
        if self.timer >= beat_time:
            self.timer = 0.0
            self.current_slot += 1
            if self.current_slot >= 8:
                self.current_slot = 0
            # change the states in the slot indicator states list (si_states)
            self.si_states[self.current_slot] = not self.si_states[self.current_slot]
            if self.current_slot != 0:
                self.si_states[self.current_slot - 1] = not self.si_states[self.current_slot - 1]
            else:
                self.si_states[7] = not self.si_states[7]
            # setting the states of the slot indicators
            for idx, si in enumerate(self.slot_indicators):
                si.set_state(state=self.si_states[idx])
            # play sound
            if self.sound_enabled:
                self.play_sound(self.current_slot)

    def draw(self) -> None:
        """ Draws the background, the arrows and lines between the arrows. """
        self.screen.blit(self.background, (0, 0))
        for i in range(8):
            if len(self.arrows) >= 8:
                self.draw_arrows(i)
            self.slot_indicators[i].render(self.screen)
            pg.draw.line(self.screen, "black", (55 + i * 60, 75), (55 + i * 60, 250), 1)
        bpm_to_blit: pg.Surface = self.font.render(str(self.bpm), True, "black")
        bpm_x_pos = 108 - bpm_to_blit.get_width() / 2  # 108 is the middle between the -1 and +1 button
        bpm_y_pos = 25 - bpm_to_blit.get_height() / 2  # 25 is the middle height of all buttons
        self.screen.blit(bpm_to_blit, (bpm_x_pos, bpm_y_pos))
        for button in self.buttons: 
            button.render(self.screen)
        self.sound_check_box.render(self.screen)
        self.strum_check_box.render(self.screen)
        self.forth_check_box.render(self.screen)
        pg.display.update()

    def run(self) -> None:
        """ Runs the Strumming Pattern Generator app. """
        old_time = perf_counter()
        while self.running:
            self.clock.tick(self.FPS)
            dt = perf_counter() - old_time
            old_time = perf_counter()
            if self.play:
                self.update_slot_indicator(dt)
            self.draw()
            self.check_elements()
            self.event_handler()
            
            

        
if __name__ == "__main__":
    generator = StrummingPatternGenerator()
    generator.run()