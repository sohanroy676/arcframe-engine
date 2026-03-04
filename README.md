# ArcFrame Engine

**ArcFrame Engine** is a lightweight, event-driven engine architecture built on top of **pygame-ce**.
It provides a clean, modular foundation for building games, simulations, and visualization tools.

The goal of ArcFrame is to bring **modern engine architecture** (event buses, scene systems, modular rendering) to pygame projects while keeping the system simple and flexible.


## Features

* **Event-driven architecture** using a central event bus
* **Scene management system** for handling multiple screens and overlays
* **Modular renderer** with a clean render loop
* **Input system** that converts pygame events into engine events
* **Decoupled systems** to keep projects maintainable
* Designed to be **lightweight and extensible**


## Architecture Overview

ArcFrame separates the core engine systems from project logic.

```
Game
 │
 └── Context
       │
       ├── EventBus
       ├── Renderer
       ├── InputSystem
       └── SceneManager
             │
             ▼
           Scenes
             │
       ┌─────┼─────┐
       ▼           ▼
      UI     Game Logic
```


## Project Structure

```
arcframe-engine/
│
├── engine/
│   ├── core/
│   │   ├── game.py
│   │   ├── context.py
│   │   └── time.py
│   │
│   ├── events/
│   │   ├── event_bus.py
│   │   └── events.py
│   │
│   ├── rendering/
│   │   └── renderer.py
│   │
│   ├── scenes/
│   │   ├── scene.py
│   │   └── scene_manager.py
│   │
│   └── input/
│       └── input_system.py
```


## Installation (Development)

Clone the repository:

```bash
git clone https://github.com/<your-username>/arcframe-engine.git
cd arcframe-engine
```

Install in editable mode:

```bash
pip install -e .
```


## Example Usage

```python
from arcframe.engine.core.game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
```


## Goals

ArcFrame is designed to:

* simplify large pygame projects
* encourage clean architecture
* support reusable engine components
* provide a foundation for games and visualization tools

## Status

**Early development**

The engine is currently under active development and the API may change.
