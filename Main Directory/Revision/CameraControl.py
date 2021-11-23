import RPi.GPIO as GPIO
#import time
#import datatime
import signal
import atexit
from picamera import PiCamera
import os

count = 0
delay = 10 # in seconds

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

def camera_control(rot1, rot2, reference):
	# Simply rotate up or down based on 'upright' orientation
        # Same thing for left and right, if we're sideways, counter that rotation
	return
