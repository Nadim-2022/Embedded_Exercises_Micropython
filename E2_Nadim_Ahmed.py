from machine import Pin, I2C, PWM
import ssd1306
from lib.led import Led

sw0 = Pin(9, Pin.IN, Pin.PULL_UP)
sw1 = Pin(8, Pin.IN, Pin.PULL_UP)
sw2 = Pin(7, Pin.IN, Pin.PULL_UP)
encoder = Pin(12, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, sda = Pin(14), scl = Pin(15))
oled = ssd1306.SSD1306_I2C(128,64,i2c)

led0 = Led(22)
led1 = Led(21)
led2 = Led(20)

def encoder_handler(pin):
    led0.off()
    led1.off()
    led2.off()
    led_state[0] = False
    led_state[1] = False
    led_state[2] = False
    display()
    
encoder.irq(handler = encoder_handler, trigger = Pin.IRQ_FALLING)

led_state = [False, False, False]
def display():
    for i in range(3):
        oled.fill_rect(0, i*10, 128, 8, 0)
        state = 'ON' if led_state[i] else 'OFF'
        oled.text(f'led{i}: {state}', 0,i*10,1)
        oled.show()

while True:
    display()
    if sw0.value() == 0 :
       led_state [0] = not led_state [0]
       led0.value(led_state[0])
       display()
       
    if sw1.value() == 0 :
       led_state [1] = not led_state [1]
       led1.value(led_state[1])
       display()
    if sw2.value() == 0 :
       led_state [2] = not led_state [2]
       led2.value(led_state[2])
       display()
       
   

