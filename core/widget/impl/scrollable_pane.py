from PIL import Image

from core.widget.impl.pane import Pane


class ScrollablePane(Pane):
    def __init__(self, height, width):
        super().__init__(height, width)
        self._x_offset = 0
        self._y_offset = 0

    def scroll_x(self, value: int) -> None:
        self._x_offset = self._x_offset + value
        self.notify_observers()

    def scroll_y(self, value: int) -> None:
        self._y_offset = self._y_offset + value
        self.notify_observers()

    def set_x_offset(self, value):
        self._x_offset = value

    def set_y_offset(self, value):
        self._y_offset = value

    def draw(self, x: int, y: int, image: Image) -> Image:
        old_image: Image = image.copy()
        for widget, x, y in self._widgets_with_position:
            image = widget.draw(x + self._x_offset, y + self._y_offset, image)

        box = (x, y, x + self._width, y + self._height)  # CHECKME
        region = image.crop(box)
        old_image.paste(region, box)
        return old_image
