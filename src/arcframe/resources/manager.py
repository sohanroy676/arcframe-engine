from pygame import Surface, Font
from pygame.image import load as load_image
from pathlib import Path

from typing import Any

class ResouceManager:
    PATH: Path = Path("assets/")
    def __init__(self) -> None:
        self._images: dict[str, Surface] = {}
        self._fonts: dict[str, Font] = {}

        self.defaults: dict[str, Any] = {"image_extension": "png"}
    
    def image(self, image_name: str, alpha: bool = True) -> Surface:
        if image_name in self._images:
            return self._images[image_name]

        image: Surface = load_image(self.PATH / "images" / f"{image_name}.{self.defaults["image_extension"]}")
        return image.convert_alpha() if alpha else image.convert()

    def destroy(self) -> None:
        pass