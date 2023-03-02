import time
from Motor import Motor

def square_movement():
    PWM = Motor()
    PWM.setMotorModel(0,0,0,0)  # Stop motors initially

    # Move the robot in a square
    for i in range(4):
        # Move forward
        PWM.setMotorModel(-1000,-1000,-1000,-1000)
        time.sleep(2)

        # Turn left
        PWM.setMotorModel(0, 0, 500, 500)
        time.sleep(2)

        # Stop
        PWM.setMotorModel(0, 0, 0, 0)
        time.sleep(5)
        
    PWM.setMotorModel(0,0,0,0)  # Stop motors after the square is complete
    
if __name__ == '__main__':
    square_movement()