from dataclasses import dataclass

@dataclass
class Config:
    width: int
    height: int
    caption: str