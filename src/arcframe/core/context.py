from arcframe.events import EventBus
from arcframe.input import InputSystem
from arcframe.rendering import Renderer
from arcframe.scenes import SceneManager
from arcframe.core.config import Config
from arcframe.resources import ResouceManager

class Context:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.bus: EventBus = EventBus()
        self.input: InputSystem = InputSystem(self.bus)
        self.renderer: Renderer = Renderer(config.width, config.height)
        self.scene_manager: SceneManager = SceneManager(self)
        self.resources: ResouceManager = ResouceManager()
    
    def destroy(self) -> None:
        self.bus.destroy()
        self.input.destroy()
        self.renderer.destroy()
        self.scene_manager.destroy()
        self.resources.destroy()