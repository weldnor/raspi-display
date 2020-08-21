from abc import ABC, abstractmethod

from core.interface.drawable import Drawable
from core.interface.observable import Observable


class Widget(Observable, Drawable, ABC):
    @abstractmethod
    def get_x(self) -> int:
        pass

    @abstractmethod
    def get_y(self) -> int:
        pass

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass

    def set_x(self, x) -> int:
        pass

    def set_y(self, y) -> int:
        pass

    def set_width(self, width) -> int:
        pass

    def set_height(self, height) -> int:
        pass
