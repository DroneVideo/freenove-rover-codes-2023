import time
from Motor import *

def leftturn():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    #Testing Turn
    PWM.setMotorModel(0, 0, -1000, -1000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)

if __name__ == '__main__':
    leftturn()