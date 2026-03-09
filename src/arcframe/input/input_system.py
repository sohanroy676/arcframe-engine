import pygame

from arcframe.events import EventBus, QuitEvent, KeyDownEvent, MouseMotionEvent, MouseButtonDownEvent

class InputSystem:
    def __init__(self, bus: EventBus) -> None:
        self.event_bus: EventBus = bus
    
    def update(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.event_bus.emit(QuitEvent())
                
                case pygame.KEYDOWN:
                    self.event_bus.emit(KeyDownEvent(event.key))
                
                case pygame.MOUSEBUTTONDOWN:
                    self.event_bus.emit(MouseButtonDownEvent(event.pos, event.button))
                
                case pygame.MOUSEMOTION:
                    self.event_bus.emit(MouseMotionEvent(event.pos, ))
    
    def destroy(self) -> None:
        '''Cleanup of external references'''
        pass