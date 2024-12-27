from button import Button
from slot_indicator import SlotIndicator

import pygame as pg

from random import choice
from typing import Final
from time import perf_counter# as pc

class StrummingPatternGenerator:
    FPS: Final[int] = 30

    def __init__(self) -> None:
        """ Initializes the Strumming Pattern Generator app. """
        pg.init()
        self.screen: pg.display = pg.display.set_mode((475, 300))
        pg.display.set_caption("Strumming Pattern Generator")

        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
        self.generate: bool = False
        self.button: Button = Button(mid_pos=(238, 25), size=(150,32))
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

    def event_handler(self) -> None:
        """ Handles events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def check_button(self) -> None:
        """ Checks if the button is clicked. """
        self.generate = self.button.check_collision()
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

    def draw(self) -> None:
        """ Draws the background, the arrows and lines between the arrows. """
        self.screen.blit(self.background, (0, 0))
        for i in range(8):
            if len(self.arrows) >= 8:
                self.draw_arrows(i)
            self.slot_indicators[i].render(self.screen)
            pg.draw.line(self.screen, "black", (55 + i * 60, 75), (55 + i * 60, 250), 1)
        self.button.render(self.screen)
        pg.display.update()

    def run(self) -> None:
        """ Runs the Strumming Pattern Generator app. """
        old_time = perf_counter()
        print(old_time)
        while self.running:
            self.clock.tick(self.FPS)
            
            self.draw()
            self.check_button()
            self.event_handler()
            

        
if __name__ == "__main__":
    generator = StrummingPatternGenerator()
    generator.run()