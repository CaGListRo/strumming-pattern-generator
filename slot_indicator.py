import pygame as pg

class SlotIndicator:
    def __init__(self, pos: tuple) -> None:
        self.pos: tuple = pos
        self.active: bool = False
        self.image: pg.Surface = pg.Surface((20, 10))

    def update(self, activated: bool=False) -> None:
        self.active = True if activated else False

    def get_state(self) -> bool:
        return self.active
 
    def render(self, surf: pg.Surface) -> None:
        self.image.fill("orange") if self.active else self.image.fill("black")
        surf.blit(self.image, self.pos)