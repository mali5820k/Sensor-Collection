import RPi.GPIO as GPIO
import time
import datatime
import signal
import atexit
from picamera import PiCamera
import os

#count = 0

def camera_capture():
	#fileName = "img_" + str(count) + ".jpg" #this stuff is to make new names for the images
	fileName = "img_" + datetime.datetime.now() + ".jpg" # Changed prev line to use current time stamp
	#count = count + 1
	os.chdir("/home/pi/Desktop/Images")
	os.system("raspistill -t 1000 -rot 180 -o " + fileName + " -w 852 -h 480") #check these args if the img is messy
	return

def camera_control(rot1, rot2, reference):
	
	return

