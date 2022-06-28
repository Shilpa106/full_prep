# Python 3 program for the above approach
S = "aaaabcc"

def isAdjChar(s):

	for i in range(len(s)-1):
	
		if (s[i] == s[i + 1]):
			return True	
	return False

def rearrangeStringUtil(N):
	global S
	S = list(S)
	
	i = 0
	j = 1
	k = 2
	
	while (k < N):		
		if (S[i] != S[j]):
			i += 1
			j += 1

			if (j == k):
				k += 1	
		else:
			if (S[j] == S[k]):			
				k += 1
			
			else:
                	
				temp = S[k]
				S[k] = S[j]
				S[j] = temp
                                
				
				i += 1
				j += 1
				
				if (j == k):
					k += 1

    # print(S)
        
	S = ''.join(S)
    

def rearrangeString(N):
	global S

	if (isAdjChar(S) == False):
		return S


	if (len(S) == 2):
		return "-1"

	
	rearrangeStringUtil(N)

	S = S[::-1]
	
	rearrangeStringUtil(N)


	if (isAdjChar(S) == False):
		return S

	return "-1"

if __name__ == '__main__':
    N = len(S)
    print(rearrangeString(N))

