import pygame
from .render_layer import RenderLayer

from typing import Callable, Any
from arcframe.types import Position, Color

type RenderCommandType = tuple[Callable, tuple[Any, ...]]

class Renderer:
    layer_order: list[RenderLayer] = sorted((layer for layer in RenderLayer), key = lambda l: l.value)
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

        self._screen = pygame.display.set_mode((width, height))

        self.clear_color: Color = (0, 0, 0)

        self._layers: dict[RenderLayer, list[RenderCommandType]] = {layer: [] for layer in self.layer_order}
        
        self.debug_value: int = 0
    
    def set_clear_color(self, new_color: Color) -> None:
        self.clear_color = new_color
    
    def begin(self) -> None:
        self._screen.fill(self.clear_color)

        for layer_queue in self._layers.values():
            layer_queue.clear()

    def _render(self) -> None:
        for layer in self.layer_order:
            for command, args in self._layers[layer]:
                command(*args)
    
    def end(self) -> None:
        self._render()
        pygame.display.flip()
    
    def submit_surface(self, surface: pygame.Surface, pos: Position = (0, 0), layer: RenderLayer = RenderLayer.WORLD) -> None:
        self._layers[layer].append((self._render_surface, (surface, pos, )))
    
    def submit_image(self, image_id, pos: Position = (0, 0)) -> None:
        pass
    
    def _render_surface(self, surface: pygame.Surface, pos: Position) -> None:
        self._screen.blit(surface, pos)
    
    def destroy(self) -> None:
        '''Cleanup of external references'''
        pass