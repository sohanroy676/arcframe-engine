from typing import Any

class Event:
    '''
    Base class for all the events
    Lower value of priority gives Higher priority 
    '''
    def __init__(self, type: str, data: Any = (), priority: int = 0) -> None:
        self.type: str = type
        self.data: Any = data

        self.priority: int = priority

    def __lt__(self, other) -> bool:
        if not isinstance(other, Event):
            return NotImplemented
        return self.priority < other.priority  

class QuitEvent(Event):
    def __init__(self) -> None:
        super().__init__("QUIT", priority=100)

class KeyDownEvent(Event):
    def __init__(self, key: Any) -> None:
        super().__init__("KEY_DOWN", (key, ))

class MouseMotionEvent(Event):
    def __init__(self, pos) -> None:
        super().__init__("MOUSE_MOTION", (pos, ))

class MouseButtonDownEvent(Event):
    def __init__(self, pos, button) -> None:
        super().__init__("MOUSE_BUTTON_DOWN", (pos, button), -1)