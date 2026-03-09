from pygame import Surface, Rect, Font, SRCALPHA, draw, image
from .element import UIElement
from arcframe.rendering import Renderer, RenderLayer

from arcframe.types import Position, Color

from typing import Callable

class Button(UIElement):
    """A UI Element to display an interactive button"""
    def __init__(self, text: str, position: Position, size: int, anchor: str = "topleft", typeface: str = "freesansbold.ttf",
                 color: Color = (255, 255, 255), bg_color: Color | None = None, z_index: int = 0, border_radius: int = -1,
                 hover_color: Color = (255, 255, 255), hover_bg_color: Color | None = None,
                 on_click: Callable | None = None) -> None:
        super().__init__(z_index)

        self.text = text
        self.font = Font(typeface, size)
        self.color = color
        self.bg_color = bg_color
        self.border_radius = border_radius
        self.anchor = anchor
        self.hover_color = hover_color
        self.hover_bg_color = hover_bg_color

        self.is_hovered: bool = False

        if on_click is not None:
            self.on_click = on_click

        self._update_surface()
        setattr(self.rect, anchor, position)
    
    def _update_surface(self) -> None:
        color: Color = self.hover_color if self.is_hovered else self.color
        bg_color: Color | None = self.hover_bg_color if self.is_hovered else self.bg_color

        surface: Surface = self.font.render(self.text, True, color)
        
        rect: Rect = surface.get_rect()
        self.rect.size = rect.size

        self.text_surface: Surface = Surface(rect.size, SRCALPHA)
        self.text_surface.convert_alpha()
        if bg_color is not None:
            draw.rect(self.text_surface, (*bg_color, 255), (0, 0, *rect.size), border_radius=self.border_radius)
        
        rect.center = (rect.width//2, rect.height//2)
        self.text_surface.blit(surface, rect)
    
    def draw(self, renderer: Renderer) -> None:
        renderer.submit_surface(self.text_surface, self.rect, RenderLayer.UI)
    
    def on_hover_enter(self) -> None:
        self.is_hovered = True
        self._update_surface()
    
    def on_hover_exit(self) -> None:
        self.is_hovered = False
        self._update_surface()
    
    def change_text(self, text: str) -> None:
        self.text = text
        self._update_surface()
    