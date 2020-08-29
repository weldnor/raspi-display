from threading import Lock

from PIL import Image
from PIL.ImageDraw import ImageDraw

from core.event.key_event import KeyEvent, KeyType
from core.interface.observer import Observer
from core.widget.impl.carousel import Carousel
from core.widget.impl.text import Text
from core.widget.impl.scrollable_pane import ScrollablePane
from core.widget.impl.multilinetext import MultilineText
from core.window.abstract_scene import AbstractScene


def clear_display(drawer: ImageDraw):
    drawer.rectangle([(0, 0), (128, 64)], fill=1)


class MyScene(AbstractScene, Observer):
    def __init__(self):
        super().__init__()
        self._lock = Lock()
        self.carousel = Carousel()
        self.carousel.subscribe(self)
        self.pane = ScrollablePane(128, 64)
        textarea = MultilineText()
        textarea.set_text('hello!\nqwerty\nasdfgh\nzxcvbn\nqwerty\nasdhfg\nmnbvbc\n')
        self.pane.add_widget(textarea, 0, 0)
        self.carousel.add_widget(self.pane)
        self.carousel.add_widget(Text("simple text"))
        self.notify_observers()

    c = 0

    def on_key_pressed(self, key_event: KeyEvent) -> None:
        with self._lock:
            print(self.c)
            self.c = self.c + 1
            if key_event.key == KeyType.KEY_RIGHT:
                self.carousel.next_widget()
            if key_event.key == KeyType.KEY_UP:
                self.pane.scroll_y(4)
            if key_event.key == KeyType.KEY_DOWN:
                self.pane.scroll_y(-4)

    def draw(self, image: Image) -> Image:
        return self.carousel.draw(0, 0, image)

    def update(self) -> None:
        self.notify_observers()
