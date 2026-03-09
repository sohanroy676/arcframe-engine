from pygame import init, Clock
from pygame.display import set_caption
from .context import Context
from .config import Config
from arcframe.events import QuitEvent

class Game:
    WIDTH: int = 1280
    HEIGHT: int = 720
    def __init__(self, config: Config) -> None:
        init()

        self.config: Config = config

        self.context: Context = Context(self.config)
        set_caption(self.config.caption)

        self.running: bool = True
        self.clock: Clock = Clock()
        self.target_fps: int = 60

        self.context.bus.subscribe(QuitEvent, self.quit)
    
    def set_initial_scene(self, scene) -> None:
        self.context.scene_manager.push_scene(scene)
    
    def quit(self) -> None:
        self.running = False
        self.context.destroy()
    
    def run(self) -> None:
        '''
        Main loop, Each frame:
        1) Takes input
        2) Notifies bus subscribers
        3) Updates the scene
        4) Draws the scene
        '''
        while self.running:
            # Setting the target fps and getting the delta time
            dt: float = self.clock.tick(self.target_fps)/1000.0

            # Takes the various events
            self.context.input.update()

            # Notifies the subscribers
            self.context.bus.process()

            # Updates the current scene
            self.context.scene_manager.update(dt)

            # Begins the drawing
            self.context.renderer.begin()

            # Draws the current scene
            self.context.scene_manager.draw()

            # Ends the drawing and renders to the screen
            self.context.renderer.end()
