from .scene import Scene
from typing import TypeAlias

SceneClass: TypeAlias = type[Scene]

class SceneManager:
    def __init__(self, context) -> None:
        self.context = context

        self._scene_stack: list[Scene] = []
    
    def _create_scene(self, scene: SceneClass) -> Scene:
        return scene(self.context)
    
    def push_scene(self, scene: SceneClass) -> None:
        self._scene_stack.append(self._create_scene(scene))
    
    def pop_scene(self) -> None:
        self._scene_stack.pop().destroy()
    
    def current_scene(self) -> Scene:
        if not self._scene_stack:
            raise RuntimeError("No active scene")
        return self._scene_stack[-1]

    def update(self, dt: float) -> None:
        self.current_scene().update(dt)
    
    def replace_current_scene(self, scene: SceneClass) -> None:
        '''Replaces the scene at the top of the scene stack with the provided scene'''
        self.pop_scene()
        self.push_scene(scene)
    
    def set_scene(self, scene: SceneClass) -> None:
        '''Cleares the scene stack and pushes the provided scene'''
        while self._scene_stack:
            self.pop_scene()
        self.push_scene(scene)
    
    def draw(self) -> None:
        for scene in self._scene_stack:
            scene.draw()
    
    def destroy(self) -> None:
        '''Cleanup of external references'''
        for scene in self._scene_stack:
            scene.destroy()
