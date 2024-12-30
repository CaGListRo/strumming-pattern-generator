import pygame as pg

from typing import Final, TypeVar

App = TypeVar("App")


class Button:
    BUTTON_COLORS: Final[dict[tuple[int]]] = {
        # Button colors including the hover, frame and shadow colors.
        'green': {'main_color': (56, 155, 60), 'hover_color': (76, 175, 80), 'shadow_color': (16, 115, 20), 'frame_color': (6, 95, 20)},
        'yellow': {'main_color': (235, 235, 0), 'hover_color': (255, 255, 50), 'shadow_color': (195, 195, 0), 'frame_color': (125, 125, 0)},
        'red': {'main_color': (235, 0, 0), 'hover_color': (255, 50, 50), 'shadow_color': (175, 0, 0), 'frame_color': (100, 0, 0)},
        'white': {'main_color': (235, 235, 235), 'hover_color': (255, 255, 255), 'shadow_color': (175, 175, 175), 'frame_color': (100, 100, 100)}
    }
    BUTTON_OFFSET: Final[int] = 5
    def __init__(self, mid_pos:tuple[int], size: tuple[int], name: str, color_schema: str) -> None:
        """
        Initialize a button object.
        Args:
        mid_pos (tuple[int]): The position of the screen on which the center of the button should sit
        size (tuple[int]): The size of the button.
        """
        self.mid_pos: tuple[int] = mid_pos
        self.size: tuple[int] = size
        self.font: pg.font.Font = pg.font.SysFont("comicsans", 23)
        self.button_text: pg.surface = self.font.render(name, True, "black")
        self.color_schema: str = color_schema
        self.click_offset: int = self.BUTTON_OFFSET
        self.bottom_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_rect: pg.Rect = pg.Rect(self.mid_pos[0] - self.size[0] / 2, self.mid_pos[1] - self.size[1] / 2, self.size[0], self.size[1])
        self.top_color: pg.Color = self.BUTTON_COLORS[self.color_schema]["main_color"]

    def check_collision(self) -> bool:
        """ Checks if the mouse is over the button and returns True if the button is clicked. """
        collided: bool = self.top_rect.collidepoint(pg.mouse.get_pos())
        if collided:
            self.top_color = self.BUTTON_COLORS[self.color_schema]["hover_color"]
            if collided and pg.mouse.get_pressed()[0]:
                self.click_offset = 0
                return True
            else:
                self.click_offset = self.BUTTON_OFFSET
                return False
        else:           
            self.top_color = self.BUTTON_COLORS[self.color_schema]["main_color"]
            self.click_offset = self.BUTTON_OFFSET
            return False

    def render(self, surf: pg.Surface) -> None:
        """
        Renders the button on the given surface.
        Args:
        surf (pg.Surface): The surface on which the button should be rendered.
        """
        border_radius: int = 5
        pg.draw.rect(surf, self.BUTTON_COLORS[self.color_schema]["shadow_color"], self.bottom_rect, border_radius=border_radius)
        pg.draw.rect(surf, self.top_color, (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius)
        surf.blit(self.button_text, (self.mid_pos[0] - self.button_text.get_width() / 2, self.mid_pos[1] - self.button_text.get_height() / 2 - self.click_offset))
        pg.draw.rect(surf, self.BUTTON_COLORS[self.color_schema]["frame_color"], (self.top_rect[0], self.top_rect[1] - self.click_offset, self.top_rect[2], self.top_rect[3]), border_radius=border_radius, width=2)
