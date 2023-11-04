from machine import Pin
import time

#led1 = Pin(22, Pin.OUT)
#led2 = Pin(21, Pin.OUT)
#led3 = Pin(20, Pin.OUT)
leds = [Pin(22, Pin.OUT), Pin(21, Pin.OUT), Pin(20, Pin.OUT)]
for led in leds:
    led.value(0)

while True:
    for led in leds:
        led.value(1)
        time.sleep(1)
        led.value(0)
    time.sleep(1)
    

