from enum import Enum, auto


class KeyType(Enum):
    KEY_UP = auto()
    KEY_DOWN = auto()
    KEY_LEFT = auto()
    KEY_RIGHT = auto()
    KEY_PRESS = auto()
    KEY1 = auto()
    KEY2 = auto()
    KEY3 = auto()


class KeyEvent:
    def __init__(self, key: KeyType):
        self.key = key
