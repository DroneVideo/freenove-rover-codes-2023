import time
from Motor import *

def stoprover(stoptime):
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(stoptime) #Stops motor for time input by user

def leftpointturn():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    PWM.setMotorModel(0, 0, -1000, -1000)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)

def rightpointturn():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    PWM.setMotorModel(-1000, -1000, 0, 0)
    time.sleep(2)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)

def rightpivotturn():
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0) # Stops motors initially

    PWM.setMotorModel(-1000, -1000, 1000, 1000)
    time.sleep(1)

    self.stoprover(1)

if __name__ == '__main__':
    stoprover(1)
    rightpivotturn
    stoprover(5)
