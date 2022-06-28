# Shortest distance from the center of a circle to a chord

# Last Updated : 07 Jun, 2022
# Given a circle which has a chord inside it. The length of the chord and the radius of the circle are given. The task is to find the shortest distance from the chord to the center.
# Examples: 

# Input: r = 4, d = 3 
# Output: 3.7081

# Input: r = 9.8, d = 7.3
# Output: 9.09492


# Approach: 

# We know that the line segment that is dropped from the center on the chord bisects the chord. The line is the perpendicular bisector of the chord, and we know the perpendicular distance is the shortest distance, so our task is to find the length of this perpendicular bisector.
# let radius of the circle = r
# length of the chord = d
# so, in triangle OBC,
# from Pythagoras theorem, 
# OB^2 + (d/2)^2 = r^2 
# so, OB = √(r^2 – d^2/4)
# So, The shortest distance from the chord to center = sqrt(r^2 - d^2/4)