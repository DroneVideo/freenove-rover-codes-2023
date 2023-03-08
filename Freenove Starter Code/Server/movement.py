import time
from Motor import *

def leftpointturn():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    #Testing Turn
    PWM.setMotorModel(0, 0, -1000, -1000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)

def rightpointturn():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    #Testing Turn
    PWM.setMotorModel(-1000, -1000, 0, 0)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)

if __name__ == '__main__':
    leftpointturn()
    rightpointturn()