# Encrypt the string - 2 

# You are given a string S. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of
#  the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it [ See the sample for more clarity ]. 
# Print the Encrypted String.

# Note: All Hexadecimal letters should be converted to Lowercase letters.

 

# Example 1:

# Input:
# S = "aaaaaaaaaaa"
# Output:
# ba 
# Explanation: 
# aaaaaaaaaaa
# Step1: a11 (a occurs 11 times)
# Step2: a11 is ab [since 11 is b in
# hexadecimal]
# Step3: ba [After reversing]
# Example 2:

# Input:
# S = "abc"
# Output:
# 1c1b1a
# Explanation: 
# abc
# Step1: a1b1c1
# Step2: 1c1b1a [After reversing]
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function encryptString() which takes a String S and returns the answer.

# Expected Time Complexity: O(|S|)
# Expected Auxiliary Space: O(1)


# Constraints
# 1 <= |S| <= 105

# S = "aaaaaaaaaaa"
# # Output:
# # ba
# # n=len(S)
# # print(hex(n)[2:]+'a')
# m=[]
# c=0
# for i in S:
#     m.append(i)
#     if i in m:
#         c+=1
# print(c)
# print(hex(c)[2:]+'a')


# 2nd
# Python3 program for the above approach

# Function to convert Decimal to Hex
def convertToHex(num):

	temp = ""
	while (num != 0):
		rem = num % 16
		c = 0
		
		if (rem < 10):
			c = rem + 48
		else:
			c = rem + 87
			
		temp += chr(c)
		num = num // 16

	return temp

# Function to encrypt the string
def encryptString(S, N):

	ans = ""

	# Iterate the characters
	# of the string
	for i in range(N):
		ch = S[i]
		count = 0

		# Iterate until S[i] is equal to ch
		while (i < N and S[i] == ch):

			# Update count and i
			count += 1
			i += 1

		# Decrement i by 1
		i -= 1

		# Convert count to hexadecimal
		# representation
		hex = convertToHex(count)

		# Append the character
		ans += ch

		# Append the characters frequency
		# in hexadecimal representation
		ans += hex

	# Reverse the obtained answer
	ans = ans[::-1]
	
	# Return required answer
	return ans

# Driver Code
if __name__ == '__main__':
	
	# Given Input
	S = "abc"
	N = len(S)

	# Function Call
	print(encryptString(S, N))

# This code is contributed by mohit kumar 29
