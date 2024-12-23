import pygame as pg

from typing import Final, TypeVar

App = TypeVar("App")


class Button:
    MAIN_COLOR: Final[tuple[int]] = (56, 155, 60)
    HOVER_COLOR: Final[tuple[int]] = (76, 175, 80) 
    SHADOW_COLOR: Final[tuple[int]] = (16, 115, 20) 
    FRAME_COLOR: Final[tuple[int]] = (6, 95, 20)
    BUTTON_OFFSET: Final[int] = 5
    def __init__(self, mid_pos:tuple[int], size: tuple[int]) -> None:
        """
        Initialize a button object.
        Args:
        mid_pos (tuple[int]): The position of the screen on which the center of the button should sit
        size (tuple[int]): The size of the button.
        """
        self.mid_pos: tuple[int] = mid_pos
        self.size: tuple[int] = size
        self.font: pg.font.Font = pg.font.SysFont("comicsans", 23)
        self.render_text()
        self.click_offset: int = self.BUTTON_OFFSET
        self.bottom_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_color: pg.Color = self.MAIN_COLOR

    def render_text(self) -> None:
        """ Renders the button text. """
        text_to_render: str = "(Re)Generate"
        self.text: pg.surface = self.font.render(text_to_render, True, "black")

    def check_collision(self) -> bool:
        """ Checks if the mouse is over the button and returns True if the button is clicked. """
        collided: bool = self.top_rect.collidepoint(pg.mouse.get_pos())
        if collided:
            self.top_color = self.HOVER_COLOR
            if collided and pg.mouse.get_pressed()[0]:
                self.click_offset = 0
                return True
            else:
                self.click_offset = self.BUTTON_OFFSET
                return False
        else:           
            self.top_color = self.MAIN_COLOR
            self.click_offset = self.BUTTON_OFFSET
            return False

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the button on the given surface.
        Args:
        surf (pg.Surface): The surface on which the button should be rendered.
        """
        border_radius: int = 5
        pg.draw.rect(surf, self.SHADOW_COLOR, self.bottom_rect, border_radius=border_radius)
        pg.draw.rect(surf, self.top_color, (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius)
        surf.blit(self.text, (self.mid_pos[0] - self.text.get_width() / 2, self.mid_pos[1] - self.text.get_height() / 2 - self.click_offset))
        pg.draw.rect(surf, self.FRAME_COLOR, (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius, width=2)
