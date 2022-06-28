# Shortest distance between a Line and a Point in a 3-D plane

# Difficulty Level : Easy
# Last Updated : 08 Feb, 2021
# Given a line passing through two points A and B and an arbitrary point C in a 3-D plane, the task is to find the shortest distance between the point C and the line passing through the points A and B.
# Examples: 

# Input: A = (5, 2, 1), B = (3, 1, -1), C = (0, 2, 3)
# Output: Shortest Distance is 5

# Input: A = (4, 2, 1), B = (3, 2, 1), C = (0, 2, 0)
# Output: Shortest Distance is 1
# Consider a point C and a line that passes through A and B as shown in the below figure.  



# Now Consider the vectors, AB and AC and the shortest distance as CD. The Shortest Distance is always the perpendicular distance. The point D is taken on AB such that CD is perpendicular to AB. 



# Construct BP and CP as shown in the figure to form a Parallelogram. Now C is a vertex of parallelogram ABPC and CD is perpendicular to Side AB. Hence CD is the height of the parallelogram.



# Note: In the case when D does not fall on line segment AB there will be a point D’ such that PD’ is perpendicular to AB and D’ lies on line segment AB with CD = PD’.
# The magnitude of cross product AB and AC gives the Area of the parallelogram. Also, the area of a parallelogram is Base * Height = AB * CD. So, 

