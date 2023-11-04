import network
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
import machine
import urequests as requests 
import ujson
from machine import Pin, I2C, PWM
import ssd1306
import math 
from math import sqrt

i2c = I2C(1, sda = Pin(14), scl = Pin(15))
oled = ssd1306.SSD1306_I2C(128,64,i2c)
#ssid ="KME551Group5" 
ssid = "TP-Link_A2FC"
password = "nadimahmed"
#password = "Groupassignment5"
def connect():
    #Connect to WLAN 
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
    
connect()


#TEST 2
def test2():
    test = [1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100]

    mean_ppi = int(1/len(test)* sum(test))
    print(mean_ppi)

    mean_hr = (((1/mean_ppi)*60)*1000)
    print(mean_hr)

    sum_rr = sum((n - mean_ppi)**2 for n in test)
    standart_deviation = math.ceil((sum_rr/(len(test)-1))**0.5)
    print(standart_deviation)

    RMSSD = sqrt(sum((test[i+1] - test[i])**2 for i in range(len(test)-1)) / (len(test)-1))
    print(RMSSD)
    oled.fill(0)
    oled.text(f"Test-1:", 0, 0)
    oled.text(f"Mean PPI: {str(mean_ppi)}", 0, 10)
    oled.text(f"Mean_HR: {str(mean_hr)}", 0, 20)
    oled.text(f"SDNN: {str(standart_deviation)}", 0, 30)
    oled.text(f"RMSSD: {str(RMSSD)}", 0, 40)
    oled.show()


#TEST 3
def test3():
    test_2 = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812, 812, 756, 820, 812, 800]
    mean_ppi_2 = int(1/len(test_2)* sum(test_2))
    print(mean_ppi_2)

    mean_hr_2 = round(((1/mean_ppi_2)*60)*1000)
    print(mean_hr_2)

    sum_rr_2 = sum((n - mean_ppi_2)**2 for n in test_2)
    standart_deviation_2 = math.ceil((sum_rr_2/(len(test_2)-1))**0.5)
    print(standart_deviation_2)


    RMSSD2 = round(sqrt(sum((test_2[i+1] - test_2[i])**2 for i in range(len(test_2)-1)) / (len(test_2)-1)))
    print(RMSSD2)
    
    oled.fill(0) 
    oled.text(f"Test-2:", 0, 0)
    oled.text(f"Mean PPI: {str(mean_ppi_2)}", 0, 10)
    oled.text(f"Mean_HR: {str(mean_hr_2)}", 0, 20)
    oled.text(f"SDNN: {str(standart_deviation_2)}", 0, 30)
    oled.text(f"RMSSD: {str(RMSSD2)}", 0, 40)
    oled.show()

while True:
    test2()
    sleep(3)
    test3() 
    sleep(3)