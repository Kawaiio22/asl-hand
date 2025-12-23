from time import sleep
from hand_servos import(
   set_positions,
   OPEN_ANGLE,
   CLOSED_ANGLE,
   THUMB_OPEN,
   THUMB_CLOSED
)
  
def letter_A():
   #fingers curled, thumb on the side
   positions={
       "thumb": THUMB_OPEN,
       "index": CLOSED_ANGLE,
       "middle": CLOSED_ANGLE,
       "ring": CLOSED_ANGLE,
       "pinky": CLOSED_ANGLE
      
       }
   set_positions(positions)
  
def letter_B():
   #Fingers straight up, thumb across palm
   positions={
       "thumb": THUMB_CLOSED,
       "index": OPEN_ANGLE,
       "middle": OPEN_ANGLE,
       "ring": OPEN_ANGLE,
       "pinky": OPEN_ANGLE
       }
   set_positions(positions)
      

