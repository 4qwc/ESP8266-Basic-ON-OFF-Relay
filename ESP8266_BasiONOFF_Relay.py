# ESP8266 Basic ON-OFF Relay
# hs4qwc 6/2/2021


from machine import Pin
import time

RLPIN_1 = 2 #output pin GPIO 2
RLPIN_2 = 16 #output pin GPIO 0
relay_1 = Pin(RLPIN_1, Pin.OUT)
relay_2 = Pin(RLPIN_2, Pin.OUT) #output pin
ON = 0
OFF = 1

relay_1.value(OFF)# set defult OFF
relay_2.value(OFF)

def turn_on():
    relay_1.value(ON)
    relay_2.value(OFF)
    print("RELAY ON")
    
def trun_off():
    relay_1.value(OFF)
    relay_2.value(ON)
    print("RELAY OFF")
    
while True:
    turn_on()
    time.sleep(5)
    trun_off()
    time.sleep(5)
