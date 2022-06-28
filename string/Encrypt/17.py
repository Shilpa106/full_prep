# Shortest distance between a point and a circle

# Last Updated : 07 Jun, 2022
# Given a circle with a given radius has its centre at a particular position in the coordinate plane. In the coordinate plane, another point is given. The task is to find the shortest distance between the point and the circle.
# Examples: 
 

# Input: x1 = 4, y1 = 6, x2 = 35, y2 = 42, r = 5 
# Output: 42.5079

# Input: x1 = 0, y1 = 0, x2 = 5, y2 = 12, r = 3
# Output: 10
 



# Approach:
 

# Let the radius of the circle = r
 

# co-ordinate of the centre of circle = (x1, y1)
 

# co-ordinate of the point = (x2, y2)
 

# let the distance between centre and the point = d
 

# As the line AC intersects the circle at B, so the shortest distance will be BC, 
# which is equal to (d-r)
 

# here using the distance formula, 
# d = √((x2-x1)^2 – (y2-y1)^2)
 

# so BC = √((x2-x1)^2 – (y2-y1)^2) – r
 

# so, 
# Shortest distance between the point and the circle = sqrt((x2-x1)^2 - (y2-y1)^2) - r     
 
