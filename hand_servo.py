from adafruit_servokit import ServoKit
import time




#16 channels PCA9685 board
kit = ServoKit(channels = 16)


servos = {
   "thumb": kit.servo[0],
   "index": kit.servo[1],
   "middle": kit.servo[2],
   "ring": kit.servo[3],
   "pinky": kit.servo[4],
   }


def open_angle():
   return 20


OPEN_ANGLE = 20
CLOSED_ANGLE = 160


THUMB_OPEN = 30
THUMB_CLOSED = 120


def set_positions(positions, delay=0.4):
  
   for finger, angle in positions.items():
       servos[finger].angle = angle
   time.sleep(delay)
  
def relax_hand():
   positions = {
       "thumb": THUMB_OPEN,
       "index": OPEN_ANGLE,
       "middle": OPEN_ANGLE,
       "ring": OPEN_ANGLE,
       "pinky": OPEN_ANGLE
       }
   set_positions(positions)


#def relax_hand(): #defines a function
#    for servo in servos.value(): #builds an array of the values in the dictionary above, and get all of the servos
#        servo.angle = 90 #move to the "middle" which is 90;
      





