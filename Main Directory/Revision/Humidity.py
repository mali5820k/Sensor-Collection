#!/usr/bin/python
import Adafruit_DHT # This library works where-as the adeept one doesn't on the pi4
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 22 # By default we should keep it to 22
failCounter = 0

def setPin(pin):
	global DHT_PIN
    DHT_PIN = pin

# Should call this once every update cycle to store in wrapper.py
def get_humidity():
    global DHT_SENSOR
    global DHT_PIN
    global failCounter

    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        #print("Temperature={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        failCounter = 0
    else:
        #print("Sensor failure. Check wiring.")
        if failCounter >= 5:
            print("Sensor Failure. Check wiring.")
        return -1
    return humidity
