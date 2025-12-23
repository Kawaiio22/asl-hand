from time import sleep
from hand_servos import relax_hand
from asl_letters import letter_A, letter_B


print("Starting now")


relax_hand()
sleep(1)




print("A")
letter_A()
sleep(2)


print("B")
letter_B()
sleep(2)


relax_hand()


print("Done")

