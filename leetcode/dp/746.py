# Minimum cost to reach the top of the floor by climbing stairs.
# Given N non-negative integers which signifies the cost of the moving from each stair.
# Paying the cost at ith step, you can either climb one or two steps.Given that  one cna start 
# from the 0-th step or 1-th step, the task is to find the min cost to reach the top of the floor
# (N+1) by climbing N stairs.

# Input: a[]={16,19,10,12,18}
# output: 31
# Start from 19 and then move to 12.

# Input: a[]={2,5,3,1,7,3,4}
# Output:9 
# 2-3-1-3

# Python3 program to find
# the minimum cost required
# to reach the n-th floor
# space-optimized solution

# function to find the minimum
# cost to reach N-th floor
def minimumCost(cost, n):

	dp1 = 0
	dp2 = 0

	# traverse till N-th stair
	for i in range(n):
		dp0 = cost[i] + min(dp1, dp2)

		# update the last
		# two stairs value
		dp2 = dp1
		dp1 = dp0
	return min(dp1, dp2)

# Driver Code
if __name__ == "__main__":
	# a = [ 2, 5, 3, 1, 7, 3, 4 ]
    a= [10,15,20]
    n=len(a)
	# n = len(a)
    print(minimumCost(a,n))
	# print(minimumCost(a, n))
	
# This code is contributed
# by ChitraNayal
