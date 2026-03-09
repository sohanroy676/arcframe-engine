from heapq import heappush, heappop
from .events import Event
from typing import Callable, Any

type ListenerDataType = tuple[Any, ...]
type ListenerType = Callable

class EventBus:
    def __init__(self) -> None:
        self.listeners: dict[type[Event], dict[int, ListenerType]] = {}
        self.queue: list[Event] = []
        self._next_id: int = 0
    
    def subscribe(self, event: type[Event], listener: ListenerType) -> int:
        '''
        Subscribes to the event bus based on the event type and returns the listner id
        '''
        listener_id: int = self._next_id
        self._next_id += 1
        
        self.listeners.setdefault(event, {})[listener_id] = listener
        
        return listener_id

    def unsubscribe(self, event: type[Event], listener_id: int) -> None:
        '''Unsubscribe from the event bus and remove listener'''
        if event in self.listeners:
            self.listeners[event].pop(listener_id, None)

    def emit(self, event: Event) -> None:
        '''Adds the event to the event queue'''
        heappush(self.queue, event)
    
    def process(self) -> None:
        '''Calls the listeners which were emitted'''
        while self.queue:
            event: Event = heappop(self.queue)

            event_type = type(event)
            if event_type not in self.listeners:
                continue

            listeners = tuple(self.listeners[event_type].values())

            for listener in listeners:
                listener(*event.data)
    
    def destroy(self) -> None:
        '''Cleanup of external references'''
        pass