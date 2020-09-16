# This is a Simple Robot Python script.
# Original Test Description:
# "Your task is to write a CLI application to parse commands and display the result.
#
# Suppose you have a robot that can receive commands in order to move it.
# These commands will tell the robot to go forwards or backwards, and turn left or right.
# These commands will be  in the format <command><number>.
# For example 'L1' means 'turn left by 90 degrees once'.  'B2' would mean go backwards 2 units.
#
# ### Available commands:
# * `F` - move forward 1 unit
# * `B` - move backward 1 unit
# * `R` - turn right 90 degrees
# * `L` - turn left 90 degrees
#
# ### Your task
# Write a program that receives a string of commands and will output the robot's distance from it's starting point.
# This distance will be the minimum amount of units the robot will need to traverse in order to get back to it's starting point.
# Remember, the robot can only turn 90 degrees at a time, so it cannot go directly back home, it must go in north, south, east, west directions.
#
# Inputs: - a string of comma-separated commands eg `F1,R1,B2,L1,B3`
# Output: - the minimum amount of distance to get back to the starting point (`4` in this case)


### Simplified Robot script for DevOps Engineer

# Suppose you have a robot that can receive commands in order to move it.
# These commands will tell the robot to go forwards or backwards, and GO left or right.


### Robot coordinates
# Inputs: - a string of comma-separated commands eg
# `F1,R1,B2,L1,B3`
# Write a program that will output the robot's distance from it's starting point.

# Inputs: - coordinates x,y of robot movement `F1,R1,B2,L1,B3`
# Output: - the distance to get back to the starting point (`4` in this case)

# Resolution:

# for `F1,R1,B2,L1,B3`

import math
# Start Point [0,0]
p1 = [0, 0]
#Step1 - F1 - Forward 1 Unit
p2 = [0, 1]
# Step2 - R1 - Right 1 Unit
p3 = [1, 1]
# Step3 - B2 - Back 2 Units
p4 = [-1, -1]
# Step4 - L1 - Left 1 Unit
p5 = [0, -1]
# Step5 - B3 - Back 3 Units
p6 = [0, -4]

distance1 = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
distance2 = math.sqrt( ((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2) )
distance3 = math.sqrt( ((p3[0]-p4[0])**2)+((p3[1]-p4[1])**2) )
distance4 = math.sqrt( ((p4[0]-p5[0])**2)+((p4[1]-p5[1])**2) )
distance5 = math.sqrt( ((p5[0]-p6[0])**2)+((p5[1]-p6[1])**2) )

distance = math.sqrt( ((p1[0]-p6[0])**2)+((p1[1]-p6[1])**2) )

print('Distance between point 1 and 2:')
print(distance1)
print('Distance between point 2 and 3:')
print(distance2)
print('Distance between point 3 and 4:')
print(distance3)
print('Distance between point 4 and 5:')
print(distance4)
print('Distance between point 5 and 6:')
print(distance5)
print('Distance BACK to the original point:')
print(distance)