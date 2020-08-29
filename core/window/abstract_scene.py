from abc import ABC, abstractmethod

from PIL import Image

from core.event.key_event import KeyEvent
from core.interface.observable import Observable


class AbstractScene(Observable, ABC):
    @abstractmethod
    def draw(self, image: Image) -> Image:
        pass

    @abstractmethod
    def on_key_pressed(self, key_event: KeyEvent) -> None:
        pass
