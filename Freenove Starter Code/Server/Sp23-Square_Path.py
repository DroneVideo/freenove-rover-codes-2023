import time
from Motor import *
from movement import * #to import turns

def square_movement():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    # Move the robot in a square
    for i in range(4):
        # Move forward
        PWM.setMotorModel(-1000,-1000,-1000,-1000)
        time.sleep(1)

        # Turn left
        leftpointturn()

        # Stop
        PWM.setMotorModel(0, 0, 0, 0)
        time.sleep(1)
        
    PWM.setMotorModel(0,0,0,0)  # Stop motors after the square is complete
    
if __name__ == '__main__':
    square_movement()