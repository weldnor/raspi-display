from abc import ABC, abstractmethod

from core.event.key_event import KeyEvent
from core.interface.drawable import Drawable
from core.interface.observable import Observable


class Window(Observable, Drawable, ABC):
    @abstractmethod
    def on_key_pressed(self, key_event: KeyEvent) -> None:
        pass
