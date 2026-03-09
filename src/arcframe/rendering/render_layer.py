from enum import Enum

class RenderLayer(Enum):
    BACKGROUND = 0
    WORLD = 10
    EFFECTS = 20
    UI = 30
    DEBUG = 40
