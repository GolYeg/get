import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
gpio.setup(leds, gpio.OUT)
gpio.setup(aux, gpio.IN)
try:
    while 1:
        for i in range(8):
            gpio.output(leds[i], gpio.input(aux[i]))
finally:
    gpio.output(leds, 0)
    gpio.cleanup()