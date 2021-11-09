
#!/usr/bin/python

import RPi.GPIO as GPIO
import time

pin =

def setPin(pin):


def get_humidity():

	channel = 18
	data = []
	j = 0

	GPIO.setmode(GPIO.BCM)

	time.sleep(1)

	GPIO.setup(channel, GPIO.OUT)

	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.02)
	GPIO.output(channel, GPIO.HIGH)

	GPIO.setup(channel, GPIO.IN)

	while GPIO.input(channel) == GPIO.LOW:
		continue

	while GPIO.input(channel) == GPIO.HIGH:
		continue

	while j < 40:
		k = 0
		while GPIO.input(channel) == GPIO.LOW:
			continue

		while GPIO.input(channel) == GPIO.HIGH:
			k += 1
			if k > 100:
				break

		if k < 8:
			data.append(0)
		else:
			data.append(1)

		j += 1

	print "sensor is working."
	print data

	humidity_bit = data[0:8]
	humidity_point_bit = data[8:16]

	humidity = 0
	humidity_point = 0
	check = 0

	for i in range(8):
		humidity += humidity_bit[i] * 2 ** (7 - i)
		humidity_point += humidity_point_bit[i] * 2 ** (7 - i)

	print "humidity : " , humidity
	return humidity
