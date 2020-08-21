import datetime
import threading

from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw

from core.widget.widget import Widget


class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class Clock(Widget):
    def __init__(self, x, y, height, width):
        super().__init__()
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        self._font = ImageFont.truetype('resources/Font.ttf', 10)
        RepeatTimer(0.8, self.update).start()

    def update(self):
        self.notify_observers()

    def draw(self, image: Image) -> Image:
        drawer = ImageDraw(image)
        now = datetime.datetime.now()
        drawer.text((self._x, self._y), now.strftime("%Y-%m-%d %H:%M:%S"), font=self._font)
        return image

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height
