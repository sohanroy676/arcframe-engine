from abc import ABC, abstractmethod

class Scene(ABC):
    '''
    Base class for all the scenes
    Required methods:
    update(self, dt: float) -> None;
    draw(self) -> None;
    destroy(self) -> None;
    '''
    def __init__(self, game_context) -> None:
        super().__init__()

        self.context = game_context
    
    @abstractmethod
    def update(self, dt: float) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def destroy(self) -> None:
        pass

    def on_switch_in(self) -> None:
        pass

    def on_switch_out(self) -> None:
        pass