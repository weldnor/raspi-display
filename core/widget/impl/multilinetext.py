import textwrap

from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw

from core.widget.abstract_widget import AbstractWidget


class MultilineText(AbstractWidget):
    def __init__(self, chars_per_string=20):
        super().__init__()
        self._text = ''
        self._chars_per_string = chars_per_string
        self._font = ImageFont.truetype('resources/Font.ttf', 8)

    def draw(self, x: int, y: int, image: Image) -> Image:
        drawer = ImageDraw(image)
        split_text = self._split_text()
        drawer.multiline_text((x, y), split_text, font=self._font, spacing=0)
        return image

    def _split_text(self):
        return textwrap.fill(self._text, width=self._chars_per_string, replace_whitespace=False)

    def set_text(self, text):
        self._text = text
        self.notify_observers()

    def append_text(self, text):
        self._text = self._text + text

    def get_text(self):
        return self._text

    # TODO
    def get_width(self) -> int:
        pass

    def get_height(self) -> int:
        pass
