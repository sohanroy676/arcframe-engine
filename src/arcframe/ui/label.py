from pygame import Surface, Rect, Font, SRCALPHA, draw
from .element import UIElement
from arcframe.rendering import Renderer, RenderLayer

from arcframe.types import Position, Color

class Label(UIElement):
    """A UI Element to display a static, non-interactive, display-only text"""
    def __init__(self, text: str, position: Position, size: int, anchor: str = "topleft", typeface: str = "freesansbold.ttf",
                 color: Color = (255, 255, 255), bg_color: Color | None = None, z_index: int = 0, border_radius: int = -1) -> None:
        super().__init__(z_index)

        self.text = text
        self.font = Font(typeface, size)
        self.color = color
        self.bg_color = bg_color
        self.border_radius = border_radius
        self.anchor = anchor

        self.is_hovered: bool = False

        self._update_surface()
        setattr(self.rect, anchor, position)

    def _update_surface(self) -> None:
        surface: Surface = self.font.render(self.text, True, self.color)
        
        rect: Rect = surface.get_rect()
        self.rect.size = rect.size

        self.text_surface: Surface = Surface(rect.size, SRCALPHA)
        self.text_surface.convert_alpha()
        if self.bg_color is not None:
            draw.rect(self.text_surface, (*self.bg_color, 255), (0, 0, *rect.size), border_radius=self.border_radius)
        
        rect.center = (rect.width//2, rect.height//2)
        self.text_surface.blit(surface, rect)

    def draw(self, renderer: Renderer) -> None:
        renderer.submit_surface(self.text_surface, self.rect, RenderLayer.UI)