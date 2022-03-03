import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

for i in range(3):
    for i in leds:
        gpio.output(i, 1)
        time.sleep(0.2)
        gpio.output(i, 0)

gpio.output(leds, 0)
gpio.cleanup()