from abc import ABCMeta, abstractmethod

from PIL import Image


class Drawable(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, image: Image) -> Image:
        pass
