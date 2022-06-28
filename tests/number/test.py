# Check Whether a number is Duck Number or not
# Input : 707069 
# Output : It is a duck number. 
# Explanation: 707069 does not contains zeros at the beginning.

# Input : 02364 
# Output : It is not a duck number. 
# Explanation: in 02364 there is a zero at the beginning of the number.
# def check_duck(num):
#     i=0
#     n=len(num)
#     while(i<n and num[i]=='0'):
#         i=i+1

#     while(i<n):
#         if(num[i]=='0'):
#             return True
#         i=i+1
#     return False


# num1='023'
# if(check_duck(num1)):
#     print('it is a duck number')
# else:
#     print('it is not a duck number')


# Round the given number to nearest multiple of 10
# Input : 4722
# Output : 4720

# Input : 38
# Output : 40

# Input : 10
# Output: 10

# Find one extra character in a string
# Input : string strA = "abcd";
#         string strB = "cbdae";
# Output : e
# string B contain all the element 
# there is a one extra character which is e

# Input : string strA = "kxml";
#         string strB = "klxml";
# Output : l
# string B contain all the element 
# there is a one extra character which is l



#  Find common elements in three sorted arrays by dictionary intersection
# Input:  ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output: [80, 20]

# Input:  ar1 = [1, 5, 5]
#         ar2 = [3, 4, 5, 5, 10]
#         ar3 = [5, 5, 10, 20]
# Output: [5, 5]

# Function to find common elements in three
# sorted arrays
from collections import Counter

def commonElement(ar1,ar2,ar3):
    # first convert lists into dictionary
	ar1 = Counter(ar1)
    
	ar2 = Counter(ar2)
	ar3 = Counter(ar3)
    # print(ar1,ar2,ar3)
	
	# perform intersection operation
	resultDict = dict(ar1.items() & ar2.items() & ar3.items())
	common = []
	print("arrrrrrrr",ar1,ar2,ar3)
	print("resultdict",resultDict)
	# iterate through resultant dictionary
	# and collect common elements
	for (key,val) in resultDict.items():
		for i in range(0,val):
			common.append(key)

	print(common)

# Driver program
if __name__ == "__main__":
	ar1 = [1, 5, 10, 20, 40, 80]
	ar2 = [6, 7, 20, 80, 100]
	ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
	commonElement(ar1,ar2,ar3)
