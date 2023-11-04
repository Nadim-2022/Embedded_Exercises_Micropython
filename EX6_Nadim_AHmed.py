import network
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
import machine
import urequests as requests 
import ujson
import ssd1306
from machine import Pin, I2C, PWM

i2c = I2C(1, sda = Pin(14), scl = Pin(15))
oled = ssd1306.SSD1306_I2C(128,64,i2c)

ssid ="KME551Group5"
#ssid = "TP-Link_A2FC"
#password = "nadimahmed"
password = "Groupassignment5"
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

response = requests.get("http://192.168.105.58:8000")

print(response.text)

def kuvios():
    APIKEY = "pbZRUi49X48I56oL1Lq8y8NDjq6rPfzX3AQeNo3a"
    CLIENT_ID = "3pjgjdmamlj759te85icf0lucv"
    CLIENT_SECRET = "111fqsli1eo7mejcrlffbklvftcnfl4keoadrdv1o45vt9pndlef"
    LOGIN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/login"
    TOKEN_URL = "https://kubioscloud.auth.eu-west-1.amazoncognito.com/oauth2/token"
    REDIRECT_URI = "https://analysis.kubioscloud.com/v1/portal/login"
    response = requests.post(
        url = TOKEN_URL,
        data = 'grant_type=client_credentials&client_id={}'.format(CLIENT_ID),
        headers = {'Content-Type':'application/x-www-form-urlencoded'},
        auth = (CLIENT_ID, CLIENT_SECRET))
    response = response.json() 
    access_token = response["access_token"] 
    intervals = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812, 812, 756, 820, 812, 800]
    data_set = {
        "type": "RRI", 
        "data": intervals, 
        "analysis": {
            "type": "readiness" 
        }
    }
    response = requests.post( 
    url = "https://analysis.kubioscloud.com/v2/analytics/analyze",
    headers = { "Authorization": "Bearer {}".format(access_token),
            "X-Api-Key": APIKEY },
            json = data_set)
    response = response.json()
   

    sns = response['analysis']['sns_index']
    pns = response['analysis']['pns_index']
    bpm = response['analysis']['mean_hr_bpm']
    
    oled.text(f"SNS: {sns}", 0,0)
    oled.text(f"PNS: {pns}", 0, 10)
    oled.text(f"BPM: {bpm}", 0, 20) 
    oled.show() 
    
    
kuvios()
