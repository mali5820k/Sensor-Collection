import RPi.GPIO as GPIO
#import time
#import datatime
from picamera import PiCamera
import os
import time

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
    # This was ~/Desktop/machineLearning/neuralNetwork -a finalNetwork.txt {}
    os.system("~/Desktop/machineLearning/neuralNetwork -a finalNetwork.txt {}".format(fileName))
    return

## Using this source for servo control:
## https://embeddedcircuits.com/raspberry-pi/tutorial/controlling-a-servo-motor-with-raspberry-pi-tutorial

# ERROR_OFFSET = 0.5
# SERVO_MIN_DUTY = 2.5 + ERROR_OFFSET # duty cycle for 0 degrees
# SERVO_MAX_DUTY = 12.5 + ERROR_OFFSET # duty cycle for 180 degrees
# MIN_ANGLE = 0 # degrees
# MAX_ANGLE = 180 # degrees
# servoBasePin = 17
# servoTopPin = 22
# refreshTime = 15 #seconds before readjusting camera
# p1 = None
# p2 = None
# lastgyroX = 0
# lastgyroY = 0 # Not using Z since z spins around vertical axis

# def setup():
#     #GPIO.setmode(GPIO.BOARD)
#     global p1, p2
#     GPIO.setmode(GPIO.BCM)

#     GPIO.setup(servoTopPin, GPIO.OUT)
#     GPIO.setup(servoBasePin, GPIO.OUT)

#     # Updated code:
#     # https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/
#     # 1ms pulse is for 0 degrees (rotate left)
#     # 1.5ms pulse is for 90 degrees (rotate to center)
#     # 2ms pulse is for 180 degrees (rotate right)
#     # 50Hz is the pwm frequency at 20ms period.
#     # duty cycle for 0 degrees = (1ms/20ms) * 100 = 5%
#     # duty cycle for 90 degrees = (1.5ms/20ms) * 100 = 7.5%
#     # duty cycle for 180 degrees = (2ms/20ms) * 100 = 10%
#     p1 = GPIO.PWM(servoTopPin, 50)
#     p2 = GPIO.PWM(servoBasePin, 50)

#     # Starting position will be centered
#     p1.start(2.5)
#     p2.start(2.5)
#     time.sleep(0.03)
#     time.sleep(0.03)
#     p1.ChangeDutyCycle(7.5) # This accepts the duty cycle in percentage form (ie 5%)
#     p2.ChangeDutyCycle(7.5) # This accepts the duty cycle in percentage form (ie 5%)


# # get the corresponding value from range 0 ~ 180 degrees to min ~ max duty cycle
# def mapValue( value, fromLow, fromHigh, toLow, toHigh):
#     return (toHigh-toLow)*(value-fromLow) / (fromHigh - fromLow) + toLow

# # rotate the servo to a specific angle
# def servoWrite(angle1, angle2):
#     global p1, p2
#     global SERVO_MIN_DUTY, SERVO_MAX_DUTY
#     global MIN_ANGLE, MAX_ANGLE

#     print("\n\nServo write")
#     # make sure it doesn't go beyond the angle the servo motor can rotate
#     if (angle1 < MIN_ANGLE):
#         p1.ChangeDutyCycle(5) # This accepts the duty cycle in percentage form (ie 5%)
#     elif (angle1 > MAX_ANGLE):
#         p1.ChangeDutyCycle(10) # This accepts the duty cycle in percentage form (ie 5%)
#     else:
#         newAngle1 = (((angle1/180) *10)/2) + 5
#         p1.ChangeDutyCycle(newAngle1)

#     if (angle2 < MIN_ANGLE):
#         p2.ChangeDutyCycle(5) # This accepts the duty cycle in percentage form (ie 5%)
#     elif (angle2 > MAX_ANGLE):
#         p2.ChangeDutyCycle(10) # This accepts the duty cycle in percentage form (ie 5%)
#     else:
#         newAngle2 = (((angle2/180) *10)/2) + 5
#         p2.ChangeDutyCycle(newAngle2)


# def camera_control(gyroscope):
#     global reference
#     global lastgyroY, lastgyroX
#     # Simply rotate up or down based on 'upright' orientation
#     # Same thing for left and right, if we're sideways, counter that rotation
#     print("\nIn camera control")
#     values = gyroscope.get("gyroscope")
#     #values = gyroscope.get("KalmanFiltered")
#     #values = gyroscope.get("Rotation")
#     angleX = values[0]
#     angleY = values[1]

#     # angleX = (angleX/2) * 180
#     # angleY = (angleY/10)

#     #print("\nangle x {}, angle y {}\n".format(angleX, angleY))

#     # diffX = abs(lastgyroX) - abs(angleX)
#     # diffY = abs(lastgyroY) - abs(angleY)

#     #while (angleX < -180):
#         #angleX += 180
#         #if (angleX >= -180):
#             #break

#     #while (angleX > 180):
#         #angleX -= 180
#         #if (angleX <= 180):
#             #break

#     #while (angleY < -180):
#         #angleY += 180
#         #if (angleY >= -180):
#             #break

#     #while (angleY > 180):
#         #angleY -= 180
#         #if (angleY <= 180):
#             #break



#     # if (angleX < -180):
#     #     diffX *= -1
#     #     if diffX < -180:
#     #         diffX = -180
#     #     angleX = diffX
#     # elif (angleX > 180):
#     #     if diffX > 180:
#     #         diffX = 180
#     #     angleX = diffX
#     # if (angleY < -180):
#     #     diffY *= -1
#     #     if diffY < -180:
#     #         diffY = -180
#     #     angleY = diffY
#     # elif (angleY > 180):
#     #     if diffY > 180:
#     #         diffY = 180
#     #     angleY = diffY

#     servoWrite(angleX, angleY)
#     # lastgyroX = angleX
#     # lastgyroY = angleY

#     return
