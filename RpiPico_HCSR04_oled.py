from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
trigger_pin=4
echo_pin=5

trigger=Pin(trigger_pin, Pin.OUT)
echo=Pin(echo_pin, Pin.IN)

WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    trigger.high()
    time.sleep_us(11)
    trigger.low()
    while (echo.value()==0):
        pass #wait for echo
    lastreadtime=time.ticks_us() # record the time when signal went HIGH
    while (echo.value()==1):
        pass #wait for echo to finish
    echotime=time.ticks_us()-lastreadtime
    if echotime>37000:
        print("No obstacle detected")
        oled.text("No obstacle detected", 0, 10)
        oled.show()
    else:
        distance = (echotime * 0.034) / 2
        print("Obstace distance= {}cm".format(distance))
        oled.text("Distance=", 0, 20)
        oled.text(str(round(distance,2)), 72, 20)
        oled.text("cm", 112, 20)
        oled.show()
    time.sleep(1)
    oled.fill(0)
    #oled.show()

