from typing import Optional, List

from PIL import Image

from core.interface.observer import Observer
from core.widget.abstract_widget import AbstractWidget


class Carousel(AbstractWidget, Observer):
    def __init__(self):
        super().__init__()
        self.widgets: List[AbstractWidget] = []
        self.current_widget: Optional[AbstractWidget] = None
        self.position = 0

    def add_widget(self, widget: AbstractWidget):
        # Подписываемся только на 1 виджет
        if len(self.widgets) == 0:
            widget.subscribe(self)
            self.current_widget = widget
        self.widgets.append(widget)

    def next_widget(self):
        self.current_widget.unsubscribe(self)

        if self.position + 1 < len(self.widgets):
            self.position = self.position + 1
        else:
            self.position = 0

        self.current_widget = self.widgets[self.position]
        self.current_widget.subscribe(self)
        self.notify_observers()

    def draw(self, x: int, y: int, image: Image) -> Image:
        if len(self.widgets) == 0:
            raise Exception("oops! no widgets to draw")

        current_widget: AbstractWidget = self.widgets[self.position]
        return current_widget.draw(x, y, image)

    def update(self) -> None:
        self.notify_observers()

    def get_width(self) -> int:
        return self.current_widget.get_width()

    def get_height(self) -> int:
        return self.current_widget.get_height()
