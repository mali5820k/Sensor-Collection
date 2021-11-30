import RPi.GPIO as GPIO
#import time
#import datatime
import signal
import atexit
from picamera import PiCamera
import os

count = 0
delay = 10 # in seconds
reference = [0, 0]

def camera_capture():
    global count
    # padded with 5 zeros: Source: https://stackoverflow.com/questions/339007/how-to-pad-zeroes-to-a-string
    #fileName = "img_" + str(count) + ".jpg" #this stuff is to make new names for the images
    #fileName = "img_" + datetime.datetime.now() + ".jpg" # Changed prev line to use current time stamp
    #fileName = "img_%05d.jpg".format(count) # can rewrite this as {n:05}
    fileName = "img_{:05d}.jpg".format(count)
    count = count + 1

    # Decided path for images:
    os.chdir("/home/pi/Desktop/Images")
    #os.system("raspistill -t 1000 -rot 180 -o " + fileName + " -w 720 -h 480")
    os.system("raspistill -t {} -rot 180 -o {} -w 720 -h 480".format(delay, fileName))

    # Running the command that Machine learning needs:
    os.system("~/Desktop/machineLearning/neuralNetwork -a FinalNetwork.txt {}".format(fileName))
    return

# Using this source for servo control:
# https://embeddedcircuits.com/raspberry-pi/tutorial/controlling-a-servo-motor-with-raspberry-pi-tutorial


ERROR_OFFSET = 0.5
SERVO_MIN_DUTY = 2.5 + ERROR_OFFSET # duty cycle for 0 degrees
SERVO_MAX_DUTY = 12.5 + ERROR_OFFSET # duty cycle for 180 degrees
MIN_ANGLE = 0 # degrees
MAX_ANGLE = 180 # degrees
servoBasePin = 17
servoTopPin = 27
pwmChannelBase = None
pwmChannelTop = None
 
def setup():    
    #initialize GPIO Pin
    #GPIO.setmode(GPIO.BOARD) 
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(servoBasePin, GPIO.OUT)
    GPIO.output(servoBasePin, GPIO.LOW)

    GPIO.setup(servoTopPin, GPIO.OUT)
    GPIO.output(servoTopPin, GPIO.LOW)
     
    # initialize PWM in defined GPIO Pin
    global pwmChannelBase
    global pwmChannelTop
    pwmChannelBase = GPIO.PWM(servoBasePin, 50)
    pwmChannelTop = GPIO.PWM(servoTopPin, 50)
    pwmChannelBase.start(0)
    pwmChannelTop.start(0)
    #servoWrite(90, 90)
 
# get the corresponding value from range 0 ~ 180 degrees to min ~ max duty cycle
def mapValue( value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow) / (fromHigh - fromLow) + toLow
     
# rotate the servo to a specific angle
def servoWrite(angle1, angle2):
    global pwmChannelBase
    global pwmChannelTop
    global SERVO_MIN_DUTY, SERVO_MAX_DUTY
    global MIN_ANGLE, MAX_ANGLE
    # make sure it doesn't go beyond the angle the servo motor can rotate
    if (angle1 < MIN_ANGLE):
        angle1 = MIN_ANGLE
    elif (angle1 > MAX_ANGLE):
        angle1 = MAX_ANGLE

    if (angle2 < MIN_ANGLE):
        angle2 = MIN_ANGLE
    elif (angle2 > MAX_ANGLE):
        angle2 = MAX_ANGLE

    pwmChannelBase.ChangeDutyCycle(map(angle1, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))
    pwmChannelTop.ChangeDutyCycle(map(angle2, 0, 180, SERVO_MIN_DUTY, SERVO_MAX_DUTY))

def camera_control(gyroscope):
    global reference
    # Simply rotate up or down based on 'upright' orientation
    # Same thing for left and right, if we're sideways, counter that rotation
    values = gyroscope.get("accelerometer")
    angleX = values[0] 
    angleY = values[1]

    if (angleX < 0):
        angleX += 180
    if (angleY < 0):
        angleY += 180

    servoWrite(angleX, angleY)

    return
