import datetime
import threading

from PIL import ImageFont, Image
from PIL.ImageDraw import ImageDraw

from core.widget.abstract_widget import AbstractWidget


class RepeatTimer(threading.Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def get_current_time_as_string() -> str:
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


class Clock(AbstractWidget):
    def __init__(self):
        super().__init__()
        self._font = ImageFont.truetype('resources/Font.ttf', 10)
        RepeatTimer(0.8, self.update).start()

    def update(self):
        self.notify_observers()

    def draw(self, x: int, y: int, image: Image) -> Image:
        drawer = ImageDraw(image)
        now = datetime.datetime.now()
        drawer.text((x, y), now.strftime("%Y-%m-%d %H:%M:%S"), font=self._font)
        return image

    # TODO check me
    def get_width(self) -> int:
        return self._font.getsize(get_current_time_as_string(), font=self._font)[0]

    def get_height(self) -> int:
        return self._font.getsize(get_current_time_as_string(), font=self._font)[1]
