##Lab 5 Part 2
##Corey Biluk

from gpiozero import PWMLED
from time import sleep
import math

led = PWMLED(17)


while True:
    for x in range (0, 157):
        led.value = math.sin(x/300)
        sleep(0.03)

