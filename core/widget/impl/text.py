from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw

from core.widget.abstract_widget import AbstractWidget


class Text(AbstractWidget):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._font = ImageFont.truetype('resources/Font.ttf', 10)

    def draw(self, x: int, y: int, image: Image) -> Image:
        drawer = ImageDraw(image)
        drawer.text((x, y), self._text, font=self._font)
        return image

    def set_text(self, text):
        self._text = text
        self.notify_observers()

    def get_text(self):
        return self._text

    def get_width(self) -> int:
        return self._font.getsize(self._text)[0]

    def get_height(self) -> int:
        return self._font.getsize(self._text)[1]
