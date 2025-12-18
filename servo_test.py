from adafruit_servokit import ServoKit
import time
#16 channels PCA9685 board
kit = ServoKit(channels = 16)
kit.servo[0].angle=0 #middle
kit.servo[3].angle = 0 
print("hi")

time.sleep(1)
kit.servo[0].angle = 180
kit.servo[3].angle = 180
print("hi again")


