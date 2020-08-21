from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw

from core.widget.widget import Widget


class Label(Widget):
    def __init__(self, x, y, text):
        super().__init__()
        self._x = x
        self._y = y
        self._text = text
        self._font = ImageFont.truetype('resources/Font.ttf', 10)

    def draw(self, image: Image) -> Image:
        drawer = ImageDraw(image)
        drawer.text((self._x, self._y), self._text, font=self._font)
        return image

    def set_text(self, text):
        self._text = text
        self.notify_observers()

    def get_text(self):
        return self._text

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return self._font.getsize(self._text)[0]

    def get_height(self) -> int:
        return self._font.getsize(self._text)[1]
