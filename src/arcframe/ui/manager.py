from arcframe.core.context import Context
from arcframe.events import MouseButtonDownEvent, MouseMotionEvent

from .element import UIElement
from .label import Label
from .button import Button

from typing import Any, Callable
from arcframe.types import Position, Color

class UIManager:
    def __init__(self, context: Context) -> None:
        self.context: Context = context

        self.elements: list[UIElement] = []

        self.hovered_element: UIElement | None = None

        # Subscribing to the event bus
        self.mouse_motion_id = context.bus.subscribe(MouseMotionEvent, self.on_mouse_motion)
        self.mouse_down_id = context.bus.subscribe(MouseButtonDownEvent, self.on_mouse_down)

        self.defaults: dict[str, Any] = {"size": 50, "anchor": "topleft", "typeface": "freesansbold.ttf",
                                         "color": (255, 255, 255), "bg_color": None, "z_index": 0, "border_radius": -1,
                                         "hover_color": (200, 200, 200), "hover_bg_color": None, "on_click": None}
    
    def set_defaults(self, *, size: int | None = None, anchor: str | None = None, typeface: str | None = None,
                     color: Color | None = None, bg_color: Color | None = None, z_index: int | None = None,
                     border_radius: int | None = None, hover_color: Color | None = None,
                     hover_bg_color: Color | None = None, on_click: Callable | None = None) -> None:
        if size is not None:
            self.defaults["size"] = size
        if anchor is not None:
            self.defaults["anchor"] = anchor
        if typeface is not None:
            self.defaults["typeface"] = typeface
        if color is not None:
            self.defaults["color"] = color
        if bg_color is not None:
            self.defaults["bg_color"] = bg_color
        if z_index is not None:
            self.defaults["z_index"] = z_index
        if border_radius is not None:
            self.defaults["border_radius"] = border_radius
        if hover_color is not None:
            self.defaults["hover_color"] = hover_color
        if hover_bg_color is not None:
            self.defaults["hover_bg_color"] = hover_bg_color
        if on_click is not None:
            self.defaults["on_click"] = on_click

    
    def add_element(self, element: UIElement) -> None:
        '''Adds the element to the elements list and orders it based on it z_index'''
        self.elements.append(element)
        
        for idx in range(len(self.elements) - 1, 0, -1):
            if self.elements[idx - 1].z_index <= self.elements[idx].z_index:
                break
            self.elements[idx - 1], self.elements[idx] = self.elements[idx], self.elements[idx - 1]
    
    def draw(self) -> None:
        '''Calls the draw methods of all the elements in the elements list'''
        for element in self.elements:
            if element.is_visible:
                element.draw(self.context.renderer)
    
    def on_mouse_down(self, pos: Position, button: int) -> None:
        '''Checks if any element is clicked and calls its on_click event handler'''
        if self.hovered_element is None or not self.hovered_element.is_enabled or not self.hovered_element.contains(pos):
            return
        
        self.hovered_element.on_click(pos, button)
    
    def on_mouse_motion(self, pos: Position) -> None:
        new_hovered: UIElement | None = None
        for element in reversed(self.elements):
            if not element.is_enabled:
                continue
            if element.contains(pos):
                new_hovered = element
                break
        
        if new_hovered is self.hovered_element:
            return
        
        if self.hovered_element is not None:
            self.hovered_element.on_hover_exit()
        
        if new_hovered is not None:
            new_hovered.on_hover_enter()
        
        self.hovered_element = new_hovered
    
    def label(self, text: str, position: Position, *, size: int | None = None, anchor: str | None = None,
              typeface: str | None = None, color: Color | None = None, bg_color: Color | None = None,
              z_index: int | None = None, border_radius: int | None = None) -> Label:
        '''
        Factory function which create a label and adds it to the elements list. Only the text and position are required.
        Remaining optional arguments are keyword-only parameters
        '''
        label: Label = Label(text, position, (self.defaults["size"] if size is None else size),
                             (self.defaults["anchor"] if anchor is None else anchor),
                             (self.defaults["typeface"] if typeface is None else typeface),
                             (self.defaults["color"] if color is None else color),
                             (self.defaults["bg_color"] if bg_color is None else bg_color),
                             (self.defaults["z_index"] if z_index is None else z_index),
                             (self.defaults["border_radius"] if border_radius is None else border_radius))
        self.add_element(label)
        return label

    def button(self, text: str, position: Position, *, size: int | None = None, anchor: str | None = None,
              typeface: str | None = None, color: Color | None = None, bg_color: Color | None = None,
              z_index: int | None = None, border_radius: int | None = None, hover_color: Color | None = None,
              hover_bg_color: Color | None = None, on_click: Callable | None = None) -> Button:
        '''
        Factory function which create a button and adds it to the elements list. Only the text and position are required.
        Remaining optional arguments are keyword-only parameters
        '''
        button: Button = Button(text, position, (self.defaults["size"] if size is None else size),
                             (self.defaults["anchor"] if anchor is None else anchor),
                             (self.defaults["typeface"] if typeface is None else typeface),
                             (self.defaults["color"] if color is None else color),
                             (self.defaults["bg_color"] if bg_color is None else bg_color),
                             (self.defaults["z_index"] if z_index is None else z_index),
                             (self.defaults["border_radius"] if border_radius is None else border_radius),
                             (self.defaults["hover_color"] if hover_color is None else hover_color),
                             (self.defaults["hover_bg_color"] if hover_bg_color is None else hover_bg_color),
                             (self.defaults["on_click"] if on_click is None else on_click))
        self.add_element(button)
        return button

    def destroy(self) -> None:
        '''Cleanup of external references'''
        self.context.bus.unsubscribe(MouseButtonDownEvent, self.mouse_down_id)