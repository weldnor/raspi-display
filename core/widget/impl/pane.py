from typing import List

from PIL import Image

from core.widget.abstract_widget import AbstractWidget


class Pane(AbstractWidget):
    def __init__(self, height, width):
        super().__init__()
        self._height = height
        self._width = width
        self._widgets_with_position: List[List[AbstractWidget, int, int]] = []

    def draw(self, x: int, y: int, image: Image) -> Image:
        old_image: Image = image.copy()
        for widget, x, y in self._widgets_with_position:
            image = widget.draw(x, y, image)

        box = (x, y, x + self._width, y + self._height)  # CHECKME
        region = image.crop(box)
        old_image.paste(region, box)
        return old_image

    def add_widget(self, widget: AbstractWidget, x: int, y: int) -> None:
        self._widgets_with_position.append([widget, x, y])
        self.notify_observers()

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height
