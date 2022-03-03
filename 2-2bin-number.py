import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 1, 1, 1, 1, 1, 1]
gpio.setup(dac, gpio.OUT)


gpio.output(dac, number)
time.sleep(10)
gpio.output(dac, 0)

gpio.cleanup()