from button import Button

import pygame as pg

from random import choice
from typing import Final

class StrummingPatternGenerator:
    FPS: Final[int] = 30

    def __init__(self) -> None:
        """ Initializes the Strumming Pattern Generator app. """
        pg.init()
        self.screen: pg.display = pg.display.set_mode((475, 250))
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
        self.background = pg.transform.scale(self.background, (475, 250))
        self.screen.blit(self.background, (0, 0))
        

    def event_handler(self) -> None:
        """ Handles events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def check_button(self) -> None:
        """ Checks if the button is clicked. """
        self.generate = self.button.check_collision()

    def generate_arrows(self) -> None:
        """ Generates arrows on the screen. """
        for i in range(4):
            draw_arrow: bool = choice((True, False))
            if draw_arrow:
                self.screen.blit(self.arrow_down, (i * 120, 50))
        for i in range(4):
            draw_arrow: bool = choice((True, False))
            if draw_arrow:
                self.screen.blit(self.arrow_up, (60 + i * 120, 50))
        self.generate = False
        

    def draw(self) -> None:
        """ Draws the background, the arrows and lines between the arrows. """
        if self.generate:
            self.screen.blit(self.background, (0, 0))
            self.generate_arrows()
        for i in range(8):
            pg.draw.line(self.screen, "black", (55 + i * 60, 50), (55 + i * 60, 223), 1)
        self.button.render(self.screen)
        pg.display.update()

    def run(self) -> None:
        """ Runs the Strumming Pattern Generator app. """
        while self.running:
            self.clock.tick(self.FPS)
            
            self.draw()
            self.check_button()
            self.event_handler()
            

        
if __name__ == "__main__":
    generator = StrummingPatternGenerator()
    generator.run()