from machine import Pin, PWM
import time


pico_led = Pin("LED", Pin.OUT)
led1 = PWM(Pin(22))
led2 = PWM(Pin(21))
led3 = PWM(Pin(20))

duty = 1000

def set_leds(value):
    led1.duty_u16(duty*(value & 0x01))
    led2.duty_u16(duty*(value & 0x02))
    led3.duty_u16(duty*(value & 0x04))


while True:
    for num in range(8):
        set_leds(num)  
        pico_led.toggle()  
        time.sleep(1) 