from button import Button
from slot_indicator import SlotIndicator

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
        #self.background = pg.transform.scale(self.background, (475, 250))
        self.screen.blit(self.background, (0, 0))
        self.arrows: list[bool] = []

        self.slot_indicators: list[SlotIndicator] = []
        for i in range(8):
            self.slot_indicators.append(SlotIndicator(pos=(14 + i * 60, 50)))
        self.si_states: list[bool] = [True, False, False, False, False, False, False, False]
        self.current_slot: int = 0
        self.bpm: int = 120
        self.timer: float = 0.0
        self.play: bool = False

    def event_handler(self) -> None:
        """ Handles events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def check_button(self) -> None:
        """ Checks if the generate_button is clicked. """
        self.generate = self.generate_button.check_collision()
        if self.generate:
            self.generate_arrows()

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

    def update_slot_indicator(self, dt: float) -> None:
        """ Updates the slot indicators. """
        beat_time: float = self.bpm / 60 / 8
        self.timer += dt
        if self.timer >= beat_time:
            self.timer = 0.0
            self.current_slot += 1
            if self.current_slot >= 8:
                self.current_slot = 0
            self.si_states[self.current_slot] = not self.si_states[self.current_slot]
            if self.current_slot != 0:
                self.si_states[self.current_slot - 1] = not self.si_states[self.current_slot - 1]
            else:
                self.si_states[7] = not self.si_states[7]
            for idx, si in enumerate(self.slot_indicators):
                si.update(activated=self.si_states[idx])


    def draw(self) -> None:
        """ Draws the background, the arrows and lines between the arrows. """
        self.screen.blit(self.background, (0, 0))
        for i in range(8):
            if len(self.arrows) >= 8:
                self.draw_arrows(i)
            self.slot_indicators[i].render(self.screen)
            pg.draw.line(self.screen, "black", (55 + i * 60, 75), (55 + i * 60, 250), 1)
        for button in self.buttons: 
            button.render(self.screen)
        pg.display.update()

    def run(self) -> None:
        """ Runs the Strumming Pattern Generator app. """
        old_time = perf_counter()
        while self.running:
            self.clock.tick(self.FPS)
            dt = perf_counter() - old_time
            old_time = perf_counter()
            self.update_slot_indicator(dt)
            self.draw()
            self.check_button()
            self.event_handler()
            
            

        
if __name__ == "__main__":
    generator = StrummingPatternGenerator()
    generator.run()