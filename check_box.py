import pygame as pg

from typing import TypeVar


class CheckBox:
    def __init__(self, font: pg.font.Font, text: str, mid_pos:tuple[int, int], images: list[pg.Surface, pg.Surface], active: bool = True) -> None:
        """
        Initialize a checkbox object.
        Args:
        font (pg.font.Font): The font to be used for the checkbox text.
        mid_pos (tuple): The middle position of the checkbox.
        images (list): A list of two images, one for the normal state and one for the.
        active (bool): Whether the checkbox is active or not. Defaults to True.
        """
        self.font: pg.font.Font = font
        self.text: str = text
        self.render_text()
        self.images: list[pg.Surface] = images
        self.half_image_width: int = self.images[0].get_width() //2
        self.mid_pos: tuple = mid_pos
        self.active: bool = active
        size: tuple = self.images[0].get_size()  
        self.clicked: bool = False
        self.rect: pg.rect = pg.Rect(self.mid_pos[0] - size[0] / 2, self.mid_pos[1] - size[1] / 2, size[0], size[1])
        self.half_text_height: float = size[1] / 2

    def render_text(self) -> None:
        """ Renders the text for the checkbox. """
        text_to_render: str = self.text
        self.text: pg.Surface = self.font.render(text_to_render, True, "black")

    def get_state(self) -> bool:
        """ Returns the state of the checkbox. """
        return self.active
    
    def set_state(self, state: bool) -> None:
        """
        Sets the state of the checkbox.
        Args:
        state (bool): The new state of the checkbox.
        """
        self.active = state

    def flip_state(self) -> None:
        """ Flips the state of the checkbox. """
        self.active = not self.active

    def check_collision(self) -> bool:
        """ Checks if the mouse is colliding with the checkbox. """
        collided: bool = self.rect.collidepoint(pg.mouse.get_pos())
        if collided:
            if collided and pg.mouse.get_pressed()[0]:
                self.clicked = True
            elif collided and self.clicked:
                self.flip_state()
                self.clicked = False
                return True
        else:           
            self.clicked = False

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the checkbox on the given surface.
        Args:
        surf (pg.Surface): The surface to render the checkbox on.
        """
        image_number: int = 0 if self.active else 1
        surf.blit(self.images[image_number], self.rect)
        surf.blit(self.text, (self.mid_pos[0] + self.half_image_width + 5, self.mid_pos[1] - self.half_text_height))
