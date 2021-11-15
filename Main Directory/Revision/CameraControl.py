import RPi.GPIO as GPIO
import time
import signal
import atexit
from picamera import PiCamera
import os

count = 0

def camera_capture():
	fileName = "img_" + str(count) + ".png" #this stuff is to make new names for the images
	count = count + 1
	os.chdir("/home/pi")
	os.system("raspistill -t 1000 -rot 180 -o " + fileName + " -w 1280 -h 960") #check these args if the img is messy
	return

def camera_control(rot1, rot2, reference):
	
	return


def main(self):


	return

if __name__ == "__main__": main()
