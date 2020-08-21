from threading import Lock

import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageDraw

from core.event.key_event import KeyEvent, KeyType
from core.window.window import Window
from lib import SH1106
from core.interface.observer import Observer

RST_PIN = 25
CS_PIN = 8
DC_PIN = 24

KEY_UP_PIN = 6
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5
KEY_RIGHT_PIN = 26
KEY_PRESS_PIN = 13

KEY1_PIN = 21
KEY2_PIN = 20
KEY3_PIN = 16


class Display(Observer):
    display: SH1106 = None
    image: Image = None
    drawer: ImageDraw = None
    lock = Lock()

    def __init__(self, window: Window):
        self.window = window
        self._init_gpio()
        self._init_display()

        window.subscribe(self)
        self.image = window.draw(self.image)

    def _init_display(self) -> None:
        self.display = SH1106.SH1106()
        self.display.Init()
        self.display.clear()
        self.image = Image.new('1', (self.display.width, self.display.height), "WHITE")
        self.drawer = ImageDraw.Draw(self.image)

    def _init_gpio(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(KEY_UP_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY_DOWN_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY_LEFT_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY_RIGHT_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY_PRESS_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY1_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY2_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)
        GPIO.add_event_detect(KEY3_PIN, GPIO.RISING, callback=self._on_key_pressed, bouncetime=200)

    def _on_key_pressed(self, code):
        if code == KEY_UP_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY_UP))
        if code == KEY_DOWN_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY_DOWN))
        if code == KEY_LEFT_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY_LEFT))
        if code == KEY_RIGHT_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY_RIGHT))
        if code == KEY_PRESS_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY_PRESS))
        if code == KEY1_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY1))
        if code == KEY2_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY2))
        if code == KEY3_PIN:
            self.window.on_key_pressed(KeyEvent(KeyType.KEY3))

    def update(self) -> None:
        with self.lock:
            self.drawer.rectangle([(0, 0), (128, 64)], fill=1)  # очищаем дисплей
            self.image = self.window.draw(self.image)
            # так так мы каждый раз обновляем изображение, то нам придется создавать новый ImageDraw
            self.drawer = ImageDraw.Draw(self.image)
            self.display.ShowImage(self.display.getbuffer(self.image))
