from abc import ABCMeta

from core.interface.observer import Observer


class Observable(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.observers = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update()
