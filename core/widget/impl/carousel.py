from typing import Optional, List

from PIL import Image

from core.interface.observer import Observer
from core.widget.widget import Widget


class Carousel(Widget, Observer):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y
        self.widgets: List[Widget] = []
        self.current_widget: Optional[Widget] = None
        self.position = 0

    def add_widget(self, widget: Widget):
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

    def draw(self, image: Image) -> Image:
        if len(self.widgets) == 0:
            raise Exception("oops! no widgets to draw")

        current_widget: Widget = self.widgets[self.position]
        current_widget.set_x(self._x)
        current_widget.set_y(self._y)
        return current_widget.draw(image)

    def update(self) -> None:
        self.notify_observers()

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_width(self) -> int:
        return self.current_widget.get_width()

    def get_height(self) -> int:
        return self.current_widget.get_height()
