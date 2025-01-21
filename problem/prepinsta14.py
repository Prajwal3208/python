
# Coding Question 14
# Instructions: You are required to write the code. You can click on compile & run anytime to check the compilation/ execution status of the program. The submitted code should be logically/syntactically correct and pass all the test cases.

# Ques: The program is supposed to calculate the distance between three points.

# For,

# x1 = 1,  y1 = 1
# x2 = 2 , y2 = 4
# x3 = 3,  y3 = 6

# Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2

import math

x1 = 1
y1 = 1
x2 = 2
y2 = 4
x3 = 3 
y3 = 6



dist1= math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
dist2= math.sqrt(math.pow(x3-x2,2) + math.pow(y3-y2,2))
dist3= math.sqrt(math.pow(x3-x1,2) + math.pow(y3-y1,2))

print(round(dist1,2), round(dist2,2), round(dist3,2))#round for round result in two decimal points