from machine import Pin
import time


pico_led = Pin("LED", Pin.OUT)
led1 = Pin(22, Pin.OUT)
led2 = Pin(21, Pin.OUT)
led3 = Pin(20, Pin.OUT)


def set_leds(value):
    led1.value(value & 0x01)
    led2.value(value & 0x02)
    led3.value(value & 0x04)


while True:
    for num in range(8):
        set_leds(num)  
        pico_led.toggle()  
        time.sleep(1)  
