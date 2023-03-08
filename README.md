# freenove-rover-codes-2023

#### Movement.py ####
In this script, we simply define simple movements to be called in other codes
Currently, we have left and right point turns that are called in square.py. They turn 90 degrees at the speed of 1000
Next step would be adding functions for stopping and left and right pivot turns. 
Next, we will modify these turn functions to take degrees as an input and modify our time to turn as required.

#### Square.py #####
In this script, we create a Motor object and define the duty cycle for each wheel to move in a square. 
We then use a for loop to move the rover forward and turn left for each side of the square. 
To turn left, we simply call the leftpointturn() function from movement.py
Finally, we stop the rover by setting the duty cycle of all motors to 0.


### Branches
Branch `create-1st-custom-path-test` is a test branch so we can edit test code without worrying about breaking anything and group changes together for documentation

To access the new branch make sure repo is up to date with `git pull` and then type `git checkout create-1st-custom-path-test`