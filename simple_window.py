from PIL import Image
from PIL.ImageDraw import ImageDraw

from core.event.key_event import KeyEvent, KeyType
from core.interface.observer import Observer
from core.widget.impl.carousel import Carousel
from core.widget.impl.clock import Clock
from core.widget.impl.label import Label
from core.window.window import Window


def clear_display(drawer: ImageDraw):
    drawer.rectangle([(0, 0), (128, 64)], fill=1)


class SimpleWindow(Window, Observer):
    def __init__(self):
        super().__init__()
        self.carousel = Carousel(20, 20)
        self.carousel.subscribe(self)
        self.carousel.add_widget(Clock(20, 20, 20, 20))
        self.carousel.add_widget(Label(20, 20, "simple text"))

    def on_key_pressed(self, key_event: KeyEvent) -> None:
        if key_event.key == KeyType.KEY_RIGHT:
            self.carousel.next_widget()

    def draw(self, image: Image) -> Image:
        return self.carousel.draw(image)

    def update(self) -> None:
        self.notify_observers()
