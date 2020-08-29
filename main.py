import time

from core.display import Display
from my_scene import MyScene

scene = MyScene()
display = Display(scene)

while 1:
    time.sleep(1)
