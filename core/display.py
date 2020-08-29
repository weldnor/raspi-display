import threading
import time
from threading import Lock

from PIL import Image
from PIL import ImageDraw
from RPi import GPIO

from core.event.key_event import KeyEvent, KeyType
from core.interface.observer import Observer
from core.window.abstract_scene import AbstractScene
from lib import SH1106

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
    def __init__(self, scene: AbstractScene):
        self._scene = scene
        self._display: SH1106 = None
        self._image: Image = None
        self._drawer: ImageDraw = None
        self._lock = Lock()

        self._init_gpio()
        self._init_display()

        scene.subscribe(self)
        self.update()

        self._listen_gpio()

    def _init_display(self) -> None:
        self._display = SH1106.SH1106()
        self._display.Init()
        self._display.clear()
        self._image = Image.new('1', (self._display.width, self._display.height), "WHITE")
        self._drawer = ImageDraw.Draw(self._image)

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

    def _listen_gpio(self):
        def loop():  # TODO refactor me!
            while True:
                if not GPIO.input(KEY_UP_PIN):
                    self._on_key_pressed(KEY_UP_PIN)
                if not GPIO.input(KEY_DOWN_PIN):
                    self._on_key_pressed(KEY_DOWN_PIN)
                if not GPIO.input(KEY_LEFT_PIN):
                    self._on_key_pressed(KEY_LEFT_PIN)
                if not GPIO.input(KEY_RIGHT_PIN):
                    self._on_key_pressed(KEY_RIGHT_PIN)
                if not GPIO.input(KEY_PRESS_PIN):
                    self._on_key_pressed(KEY_PRESS_PIN)
                if not GPIO.input(KEY1_PIN):
                    self._on_key_pressed(KEY1_PIN)
                if not GPIO.input(KEY2_PIN):
                    self._on_key_pressed(KEY2_PIN)
                if not GPIO.input(KEY3_PIN):
                    self._on_key_pressed(KEY3_PIN)
                time.sleep(0.1)

        t = threading.Thread(loop())
        t.start()

    def _on_key_pressed(self, code):
        if code == KEY_UP_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY_UP))
        if code == KEY_DOWN_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY_DOWN))
        if code == KEY_LEFT_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY_LEFT))
        if code == KEY_RIGHT_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY_RIGHT))
        if code == KEY_PRESS_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY_PRESS))
        if code == KEY1_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY1))
        if code == KEY2_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY2))
        if code == KEY3_PIN:
            self._scene.on_key_pressed(KeyEvent(KeyType.KEY3))

    def update(self) -> None:
        with self._lock:
            self._drawer.rectangle([(0, 0), (128, 64)], fill=1)  # очищаем дисплей
            self._image = self._scene.draw(self._image)
            # так так мы каждый раз обновляем изображение, то нам придется создавать новый ImageDraw
            self._drawer = ImageDraw.Draw(self._image)
            self._display.ShowImage(self._display.getbuffer(self._image))
