from machine import Pin, I2C, PWM
import ssd1306
from time import sleep

class led_control:
    def __init__(self):
        self.led1 = PWM(Pin(22, Pin.OUT))
        self.led2 = PWM(Pin(21, Pin.OUT))
        self.led3 = PWM(Pin(20, Pin.OUT))
        self.menu = 0
        #self.mainmenu = 0
        self.count = 0
        self.pcount = 0
        self.led = 0
        self.ledcount = 1
        self.i2c = I2C(1, sda = Pin(14), scl = Pin(15))
        self.oled = ssd1306.SSD1306_I2C(128,64,self.i2c)
        self.rota = Pin(10, Pin.IN, Pin.PULL_UP)
        self.rotb = Pin(11, Pin.IN, Pin.PULL_UP)
        self.rotp = Pin(12, Pin.IN, Pin.PULL_UP)
        self.rota.irq(handler = self.encoder, trigger = Pin.IRQ_FALLING)
        #self.rotb.irq(handler = self.encoder, trigger = Pin.IRQ_FALLING)
        self.rotp.irq(handler = self.rotpush, trigger = Pin.IRQ_FALLING)
        self.duty = 0
        self.duty_1 = 0
        self.duty_2 = 0
        self.duty_3 = 0
        self.brightness = (self.duty/5000)*100
        self.bar_size = int(self.brightness/100*128)
        self.brightness_1 = (self.duty_1/5000)*100
        self.bar_size_1 = int(self.brightness_1/100*128)
        self.brightness_2 = (self.duty_2/5000)*100
        self.bar_size_2 = int(self.brightness_2/100*128)
        self.brightness_3 = (self.duty_3/5000)*100
        self.bar_size_3 = int(self.brightness_3/100*128)
        
        
    def rotpush(self, pin):
        if not self.rotp.value():
            self.pcount += 1
            if self.pcount > 1:
                self.pcount = 1
        print("pcount",self.pcount)
        #sleep(2)
        
        
    def encoder(self, pin):
        if self.rotb.value() :
            self.count += 1
            if self.count > 1:
                self.count = 1
        else:
            self.count -= 1
            if self.count < 0:
                self.count = 0
        #sleep(0.10)
        self.led_britness()
        self.led_menu_selection()

        print("menu:",self.menu)
        #self.led_britness()
        #self.pcount = 0  
        print(self.count)
        #print(self.mainmenu)
        #print(self.led)
    def led_britness(self):
        if self.menu == 1:
            if self.count == 1:
                self.duty += 1000
                if self.duty > 5000:
                    self.duty = 5000
            else:
                self.duty -= 1000
                if self.duty < 0:
                    self.duty = 0
        self.brightness = (self.duty/5000)*100
        self.bar_size = int(self.brightness/100*128)
        if self.menu == 3:
            if self.ledcount == 1:
                if self.count == 1:
                    self.duty_1 += 1000
                    if self.duty_1 > 5000:
                        self.duty_1 = 5000
                else:
                    self.duty_1 -= 1000
                    if self.duty_1 < 0:
                        self.duty_1 = 0
            self.brightness_1 = (self.duty_1/5000)*100
            self.bar_size_1 = int(self.brightness_1/100*128)
            if self.ledcount == 2:
                if self.count == 1:
                    self.duty_2 += 1000
                    if self.duty_2 > 5000:
                        self.duty_2 = 5000
                else:
                    self.duty_2 -= 1000
                    if self.duty_2 < 0:
                        self.duty_2 = 0
            self.brightness_2 = (self.duty_2/5000)*100
            self.bar_size_2 = int(self.brightness_2/100*128)
            if self.ledcount == 3:
                if self.count == 1:
                    self.duty_3 += 1000
                    if self.duty_3 > 5000:
                        self.duty_3 = 5000
                else:
                    self.duty_3 -= 1000
                    if self.duty_3 < 0:
                        self.duty_3 = 0
            self.brightness_3 = (self.duty_3/5000)*100
            self.bar_size_3 = int(self.brightness_3/100*128)
        #print(self.duty)
    def led_menu_selection(self):
        if self.menu == 2:
                if self.count == 1:
                    self.led +=1
                    if self.led > 4:
                        self.led = 4
                else:
                    self.led -= 1
                    if self.led < 0:
                        self.led = 0
    def menu_selection(self):
        if self.menu == 0 and self.mainmenu == 1 and self.pcount == 1 and self.count == 0:
            self.menu = 2
            self.pcount = 0
        if self.menu == 0 and self.mainmenu == 2 and self.pcount == 1 and self.count == 1:
            self.menu = 1
            self.pcount = 0
        if self.menu == 1 and self.mainmenu == 2 and self.pcount == 1:
            self.menu = 0
            self.pcount = 0
        if self.menu == 2 and self.ledcount == 4 and self.pcount == 1:
            self.pcount = 0
            self.menu = 0
        if self.menu == 2 and self.ledcount == 1 and self.pcount == 1:
            self.menu = 3
            self.pcount = 0
        if self.menu == 3 and self.pcount == 1:
            self.menu = 2
            self.pcount = 0
        if self.menu == 2 and self.ledcount == 2 and self.pcount == 1:
            self.menu = 3
            self.pcount = 0
        if self.menu == 2 and self.ledcount == 3 and self.pcount == 1:
            self.menu = 3
            self.pcount = 0
            
               
    def display(self):
        self.oled.fill(0)
        if self.menu == 0:
            if self.menu == 0 and self.count == 0:
                self.oled.fill_rect(0,0,128,8,1)
                self.oled.text('LED MODE', 0,0,0)
                self.oled.text('BTITNESS MODE', 0,10,1)
                self.oled.show()
                self.mainmenu = 1
            if self.menu == 0 and self.count == 1:
                self.oled.fill_rect(0,10,128,8,1)
                self.oled.text('LED MODE', 0,0,1)
                self.oled.text('BRIGHTNESS MODE', 0,10,0)
                self.oled.show()
                self.mainmenu = 2
        if self.menu == 1:
            self.oled.fill(0)
            self.oled.rect(0, 0, 128, 20, 1)
            self.oled.fill_rect(0, 0, self.bar_size, 20, 1)
            self.oled.text(str(self.brightness) + "%", 0, 30)
            self.oled.show()
            if self.brightness >= 70:
                sleep(0.5)
                self.oled.text(str("TOO High"), 0, 40)
                self.oled.show()
                sleep(0.5)
                
                    
            #print(bar_size)
            self.led1.duty_u16(self.duty)
            self.led2.duty_u16(self.duty)
            self.led3.duty_u16(self.duty)
        if self.menu == 2:
            if self.led == 0:
                self.oled.fill_rect(0,0,128,8,1)
                self.oled.text('LED 1', 0,0,0)
                self.oled.text('LED 2', 0,10,1)
                self.oled.text('LED 3', 0,20,1)
                self.oled.text('BACK', 0,30,1)
                self.oled.show()
                
                
                self.ledcount = 1
            
            if self.led == 1:
                self.oled.fill_rect(0,10,128,8,1)
                self.oled.text('LED 1', 0,0,1)
                self.oled.text('LED 2', 0,10,0)
                self.oled.text('LED 3', 0,20,1)
                self.oled.text('BACK', 0,30,1)
                self.oled.show()
                
                self.ledcount = 2
            
            if self.led == 2:
                self.oled.fill_rect(0,20,128,8,1)
                self.oled.text('LED 1', 0,0,1)
                self.oled.text('LED 2', 0,10,1)
                self.oled.text('LED 3', 0,20,0)
                self.oled.text('BACK', 0,30,1)
                self.oled.show()
                
                self.ledcount = 3
            if self.led == 3:
                self.oled.fill_rect(0,30,128,8,1)
                self.oled.text('LED 1', 0,0,1)
                self.oled.text('LED 2', 0,10,1)
                self.oled.text('LED 3', 0,20,1)
                self.oled.text('BACK', 0,30,0)
                self.oled.show()
                self.ledcount = 4
        if self.menu == 3:
            if self.ledcount == 1:
                self.oled.fill(0)
                self.oled.rect(0, 0, 128, 20, 1)
                self.oled.fill_rect(0, 0, self.bar_size_1, 20, 1)
                self.oled.text(str(self.brightness_1) + "%", 0, 30)
                self.oled.show()
                if self.brightness_1 >= 70:
                    sleep(0.5)
                    self.oled.text(str("TOO High"), 0, 40)
                    self.oled.show()
                    sleep(0.5)
                #print(bar_size_1)
                self.led1.duty_u16(self.duty_1)
            if self.ledcount == 2:
                self.oled.fill(0)
                self.oled.rect(0, 0, 128, 20, 1)
                self.oled.fill_rect(0, 0, self.bar_size_2, 20, 1)
                self.oled.text(str(self.brightness_2) + "%", 0, 30)
                self.oled.show()
                if self.brightness_2 >= 70:
                    sleep(0.5)
                    self.oled.text(str("TOO High"), 0, 40)
                    self.oled.show()
                    sleep(0.5)
                #print(bar_size_1)
                self.led2.duty_u16(self.duty_2)
            if self.ledcount == 3:
                self.oled.fill(0)
                self.oled.rect(0, 0, 128, 20, 1)
                self.oled.fill_rect(0, 0, self.bar_size_3, 20, 1)
                self.oled.text(str(self.brightness_3) + "%", 0, 30)
                self.oled.show()
                if self.brightness_3 >= 70:
                    sleep(0.5)
                    self.oled.text(str("TOO High"), 0, 40)
                    self.oled.show()
                    sleep(0.5)
                #print(bar_size_1)
                self.led3.duty_u16(self.duty_3)           
        self.menu_selection()
        

me = led_control()
while True:
    me.display()
    #me.menu_selection()
    

    
    
            
                    
                
            
        
        

