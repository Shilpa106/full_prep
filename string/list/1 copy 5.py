# Convert delimiter separated Mixed String to valid List

# Last Updated : 15 Jul, 2021
# Given a string with elements and delimiters, split elements on delimiter to extract with elements ( including containers).

# Input : test_str = “6*2*9*[3, 5, 6]*(7, 8)*8*4*10”, delim = “*” 
# Output : [6, 2, 9, [3, 5, 6], (7, 8), 8, 4, 10] 
# Explanation : Containers and elements separated using *.

# Input : test_str = “[3, 5, 6]*(7, 8)*8*4*10”, delim = “*” 
# Output : [[3, 5, 6], (7, 8), 8, 4, 10] 
# Explanation : Containers and elements separated using *. 