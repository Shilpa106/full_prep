# Minimize Cost to sort a String in Increasing Order of Frequencies of Characters

# Difficulty Level : Medium
# Last Updated : 20 Apr, 2021
# Given a string S, the task is to calculate the minimum cost to sort the string in increasing order of their frequencies by swapping a block of repeated characters with another block of different repeated characters. The cost of each operation is the absolute difference of the two blocks.
# Examples: 

# Input: S = “aabbcccdeffffggghhhhhii” 
# Output: 5 
# Explanation: 

# Swap ‘d’ with ‘aa’. The Cost of this Operation is 1
# Swap ‘e’ with ‘bb’. The Cost of this Operation is 1
# Swap ‘ii’ with ‘ccc’. The Cost of this Operation is cost is 1
# Swap ‘ccc’ with ‘ffff’. The Cost of this Operation is 1
# Swap ‘ffff’ with ‘hhhhh’. The Cost of this Operation is 1
# Input : S = “aaaa” 
# Output : 0 

 
# Approach: 
#  Follow the steps below to solve the problem:

# Store the frequency of each character present in the String.
# Sort the frequencies.
# Calculate the difference between each frequency in the sorted and original sequence.
# Half of the total sum of all the differences is the required answer. This is because, for each swap, the difference is calculated twice in the above step.
