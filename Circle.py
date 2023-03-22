import time
from Motor import *


def circle():
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)
    for _ in range(2):
        PWM.setMotorModel(500, 1000, -2000, -2000)
        time.sleep(2)
        PWM.setMotorModel(0, 0, 0, 0)
    PWM.setMotorModel(0, 0, 0, 0)

if __name__ == '__main__':
    circle()
