# Minimum distance a person has to move in order to take a picture of every racer

# Last Updated : 05 Aug, 2021
# Consider a linear running track. Some racers are running on the track between a particular segment. A person is trying to take pictures of every racer. The person can take a picture of a racer if he stands anywhere between the racer’s running track segment i.e. between the start and end point of the racer. Given the starting and ending point of N racers and an integer D denoting the initial position of the person taking pictures. The task is to find the minimum distance the person has to move in order to take the picture of every racer from the final point. If it is impossible to take the pictures of every racer than print -1.

# Examples: 

# Input: start[] = {0, 2, 4}, end[] = {7, 14, 6}, D = 3 
# Output: 1 
# The segments are: 
# 0 . . . . . . 7 
# . . 2 . . . . . . . . . . . 14 
# . . . . 4 . 6 
# . . . d 
# Hence, the person has to move towards 4 i.e. 1 unit.

# Input: start[] = {1, 2}, end[] = {2, 3}, D = 2 
# Output: 0 

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Approach: The above problem can be solved by observation, that the person has to be ahead of each racer before they start the race and finish it. So if he is in the range of the racer starting last and the racer ending first, he can take the picture, else not.
# Find the maximum value of the starting point say left and the minimum value of the ending point say right among all the given racers. Now, 

# left > right then it is impossible for the person to take pictures and print -1.
# If D is within the range [left, right] then the person doesn’t need to move and the answer will be 0.
# Else the person has to move min(abs(left – D), abs(right – D)).
