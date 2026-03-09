from pygame import Rect

from arcframe.types import Position

class UIElement:
    def __init__(self, z_index: int = 0) -> None:
        self.is_visible: bool = True
        self.is_enabled: bool = True
        self.z_index: int = z_index

        self.rect: Rect = Rect()
    
    def draw(self, renderer) -> None:
        pass

    def update(self) -> None:
        pass

    def on_click(self, pos: Position, button: int) -> None:
        pass

    def on_release(self, pos: Position, button: int) -> None:
        pass

    def contains(self, pos: Position) -> bool:
        return self.rect.collidepoint(pos)
    
    def on_hover_enter(self) -> None:
        pass

    def on_hover_exit(self) -> None:
        pass