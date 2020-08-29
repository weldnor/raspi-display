from abc import ABC, abstractmethod

from PIL import Image

from core.interface.observable import Observable


class AbstractWidget(Observable, ABC):
    @abstractmethod
    def draw(self, x: int, y: int, image: Image) -> Image:
        pass

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass
