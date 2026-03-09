import pygame
from typing import Any, Generator

def draw_grid_lines(surf: pygame.Surface, rows: int, cols: int, side_length: int, color: tuple[int], update=False) -> None:
    for i in range(rows + 1):
        pygame.draw.line(surf, color, (0, i*side_length), (cols*side_length, i*side_length))
    for i in range(cols + 1):
        pygame.draw.line(surf, color, (i*side_length, 0), (i*side_length, rows*side_length))
    if update: pygame.display.update()

def HSV_to_RGB(h: float, s: float, v: float) -> tuple[int | float, int | float, int | float]:
    c = v*s
    x = c * (1 - abs((h/60) % 2 - 1))
    m = abs(v - c)
    if h < 60: rgb = (c, x, 0)
    elif h < 120: rgb = (x, c, 0)
    elif h < 180: rgb = (0, c, x)
    elif h < 240: rgb = (0, x, c)
    elif h < 300: rgb = (x, 0, c)
    else: rgb = (c, 0, x)
    return ((rgb[0]+m)*255, (rgb[1]+m)*255, (rgb[2]+m)*255)

def lerp(a: int | float, b: int | float, t: int | float) -> int | float:
    '''Linear Interpolation'''
    return (1 - t) * a + t * b

def inv_lerp(a: int | float, b: int | float, v: int | float) -> float:
    '''Inverse Linear Interpolation'''
    return (v - a) / (b - a)


def remap(i_min: float, i_max: float, o_min: float, o_max: float, v: float) -> float:
    return lerp(o_min, o_max, inv_lerp(i_min, i_max, v))

def rot_center(image, angle: float, x: int, y: int) -> tuple:
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return (rotated_image, new_rect)

def blitRotateCenter(surf, image, topleft, angle: float):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    return surf.blit(rotated_image, new_rect)

class Vector2:
    def __init__(self, x: int | float, y: int | float):
        self.x: int | float = x
        self.y: int | float = y
    
    def get_pos(self) -> list[int | float]:
        return [self.x, self.y]
    
    def __add__(self, other: Vector2):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    
    def __mul__(self, other: int | float):
        if isinstance(other, int | float):
            return Vector2(self.x * other, self.y * other)
        else:
            return NotImplemented
    
    def __iter__(self) -> Generator[int | float, Any, None]:
        yield self.x
        yield self.y
    
    def __repr__(self) -> str:
        return f"Vec2(x = {self.x}, y = {self.y})"