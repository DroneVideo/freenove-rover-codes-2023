import time
from Motor import *


def stoprover(stoptime):
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(stoptime)  # Stops motor for time input by user


def leftpointturn(theta):
    frac = theta / 90  # theta in degree
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)  # Stop motors initially

    PWM.setMotorModel(0, 0, -1000, -1000)
    time.sleep(2 * frac)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)


def rightpointturn(theta):
    frac = theta / 90  # theta in degree
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)  # Stop motors initially

    PWM.setMotorModel(-1000, -1000, 0, 0)
    time.sleep(2 * frac)
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)


def rightpivotturn(theta):
    frac = theta / 90  # theta in degree
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)  # Stops motors initially

    PWM.setMotorModel(-1000, -1000, 1000, 1000)
    time.sleep(1.5 * frac)  # theta in degree)

    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)


def leftpivotturn(theta):
    frac = theta / 90  # theta in degree
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)  # Stops motors initially

    PWM.setMotorModel(1000, 1000, -1000, -1000)
    time.sleep(1.5 * frac)

    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1)


def move_distance(dist, direction='forward'):
    '''
    dist is in cm
    '''
    temp = dist / 35
    PWM = Motor()
    PWM.setMotorModel(0, 0, 0, 0)  # Stops motors initially
    if direction == 'forward':
        PWM.setMotorModel(-1000, -1000, -1000, -1000)
        time.sleep(1 * temp)
    elif direction == 'back':
        PWM.setMotorModel(1000, 1000, 1000, 1000)
        time.sleep(1)

    # stops motors afterward
    PWM.setMotorModel(0, 0, 0, 0)
    time.sleep(1 * temp)


if __name__ == '__main__':
    stoprover(1)
    move_distance(100, 'forward')
    stoprover(0.5)
    move_distance(50, 'back')
    stoprover(1)
    for _ in range(50):
        move_distance(1)
        stoprover(0.1)

    # stoprover(1)
    # rightpointturn(45)
    # stoprover(1)
    # leftpointturn(135)
    # stoprover(1)
    # rightpivotturn(45)
    # stoprover(1)
    # leftpivotturn(135)
    # stoprover(1)
