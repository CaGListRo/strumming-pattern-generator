import pygame as pg

from random import choice
from typing import Final

class StrummingPatternGenerator:
    FPS: Final[int] = 30

    def __init__(self) -> None:
        """ Initializes the Strumming Pattern Generator app. """
        pg.init()
        self.screen: pg.display = pg.display.set_mode((480, 223))
        pg.display.set_caption("Strumming Pattern Generator")

        self.running: bool = True
        self.clock: pg.time.Clock = pg.time.Clock()
        self.generate: bool = True
        # load images
        self.arrow_down: pg.Surface = pg.image.load("arrow.png").convert_alpha()
        self.arrow_up: pg.Surface = pg.image.load("arrow.png").convert_alpha()
        self.arrow_up = pg.transform.rotate(self.arrow_up, 180)
        self.background: pg.Surface = pg.image.load("background.png")
        

    def event_handler(self) -> None:
        """ Handles events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()

    def generate_arrows(self) -> None:
        """ Generates arrows on the screen. """
        for i in range(4):
            draw_arrow: bool = choice((True, False))
            if draw_arrow:
                self.screen.blit(self.arrow_down, (i * 100, 25))
        for i in range(4):
            draw_arrow: bool = choice((True, False))
            if draw_arrow:
                self.screen.blit(self.arrow_up, (50 + i * 100, 25))
        self.generate = False
        

    def draw(self) -> None:
        """ Draws the background, the arrows and lines between the arrows. """
        if self.generate:
            self.screen.blit(self.background, (0, 0))
            self.generate_arrows()
            for i in range(8):
                pg.draw.line(self.screen, "black", (50 + i * 50, 25), (50+ i * 50, 223), 1)
        pg.display.update()

    def run(self) -> None:
        """ Runs the Strumming Pattern Generator app. """
        while self.running:
            self.clock.tick(self.FPS)
            self.draw()
            self.event_handler()
            

        
if __name__ == "__main__":
    generator = StrummingPatternGenerator()
    generator.run()