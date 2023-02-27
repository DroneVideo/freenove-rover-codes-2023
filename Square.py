import time
from motor import Motor

def square():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    # Move the robot in a square
    for i in range(4):
        # Move forward
        PWM.setMotorModel(2000,2000,2000,2000)
        time.sleep(2)

        # Turn left
        PWM.setMotorModel(-500,-500,2000,2000)
        time.sleep(1.5)

        # Stop
        PWM.setMotorModel(0, 0, 0, 0)
        time.sleep(1)
        
    PWM.setMotorModel(0,0,0,0)  # Stop motors after the square is complete
    
if __name__ == '__main__':
    square_movement()