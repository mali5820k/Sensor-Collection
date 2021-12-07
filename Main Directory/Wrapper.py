import RPi.GPIO as GPIO
import sys # Comment this line out for debugging to purposefully cause an error
import Humidity
import CameraControl
import GPS
import Gyroscope
import Temperature
import socket 
import time

##########################################################
import json

# Sensors Data buffer
dataBuffer = {}


# For sending GPS data to command and telemetry
def tojson(data:dict):
        jsonString = json.dump(data)
        return jsonString

# Input should be the jsonString the above function returns
# also, need to check if open-socket was successfulu or not, if not, don't do anything.
def sendData(input: str):
    host = '127.0.0.1'
    port = 25565
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))
    input.encode("utf-8", "strict")
    sendingBytes = bytes(input, "utf-8")
    socket.sendall(sendingBytes)
    
    
##########################################################


def init_DHT_11():
    Humidity.setPin(27)


def init_Berry_gps():
    GPS.connectBus()
    GPS.firstRun = False

def init_Berry_Accel_Gyro_Compass():
    Gyroscope.init_sensors()

def init_Berry_temperature():
    pass

def init_cam_ctrl():
    # Zero out camera
    #CameraControl.setup() # Borked camera control
    pass
    

# These two inits are special and can exit the system if
# any of the above inits causes an error.

def init_all_sensors():
    init_Berry_Accel_Gyro_Compass()
    init_DHT_11()
    init_Berry_gps()
    init_Berry_temperature()
    init_cam_ctrl()

# Functions to get parameters for every sensor's data
# Return a -1 if not successful
def get_humidity():
    global dataBuffer
    humidity = Humidity.get_humidity()
    dataBuffer["Humidity"] = humidity
    #dataBuffer.update(humidity)


def get_temperature_Altitude_Pressure():
    global dataBuffer
    readVal = Temperature.getTemperaturePressureAltitude()
    # dataBuffer["Temperature"] = readVal["Temperature"]
    # dataBuffer["Altitude"] = readVal["Altitude"]
    # dataBuffer["Pressure"] = readVal["Pressure"]
    dataBuffer.update(readVal)
    pass


# Do not call this function, this will hang the program
def get_gps_position():
    global dataBuffer
    readVal = GPS.readGPS()
    dataBuffer.update(readVal)
    pass


def get_gscope_Accel_KalmanFiltered():
    global dataBuffer
    gyroAccKalman = Gyroscope.getGyroAccelMagno()
    # dataBuffer["Gyroscope"] = gyroAccKalman["gyroscope"]
    # dataBuffer["Accelerometer"] = gyroAccKalman["accelerometer"]
    # dataBuffer["KalmanFiltered"] = gyroAccKalman["KalmanFiltered"]
    dataBuffer.update(gyroAccKalman)


def capture_image():
    #CameraControl.camera_control(dataBuffer)
    # Camera Control is not functioning properly, need to use different approach
    CameraControl.camera_capture()
    pass


def main():
    global dataBuffer
    init_all_sensors()

    while(True):
        get_humidity()
        get_temperature_Altitude_Pressure()
        get_gscope_Accel_KalmanFiltered()
        capture_image()
        get_gps_position()
        for key, value in dataBuffer.items():
            print("{} {}".format(key, value))
        else:
            print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup() # Humidity and Camera may be using GPIO.
        print("Keyboard interrupt triggered! Quitting Wrapper.py")
        sys.exit(1) # If not 0, then we borked, so restart the wrapper
    except Exception:
        sys.exit(1) # Something is broken, restart script