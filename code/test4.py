# Python program for rearranging characters in a string such
# that no two adjacent are same

# Function to find the char with maximum frequency in the given
# string
def getMaxCountChar(count):
    maxCount = 0
    for i in range(26):
        if count[i] > maxCount:
            # print("10",count[0])
            maxCount = count[i]
            # print("12",maxCount)
            # ascii a=97
            print("14",i)
            maxChar = chr(i + ord('a'))
            # print("15",chr(i))
            # print("16",ord('a'))
            # print("15",chr(1 + ord('a')))
    # print("19",maxCount)
            # print("16",maxChar)

    return maxCount, maxChar

# Main function for rearranging the characters
def rearrangeString(S):
    n = len(S)

    # if length of string is None return False
    if not n:
        return False
        
    # create a hashmap for the alphabets
    count = [0] * 26
    # print("34",count)
    for char in S:
        # print("36",count)
        count[ord(char) - ord('a')] += 1
        # print("29",ord(char))
        # print("30",ord('a'))
        # print("31",count[0])
        # print("41",count)
    # print(count):""
    # print("28",getMaxCountChar(count))

    maxCount, maxChar = getMaxCountChar(count)

    # if the char with maximum frequency is more than the half of the
    # total length of the string than return False
    if maxCount > (n + 1) // 2:
        return False

    # create a list for storing the result
    res = [None] * n
    # res = [8] * 5
    
    # print("522222",res)

    ind = 0

    # place all occurrences of the char with maximum frequency in
    # even positions
    # print("61",maxCount)
    while maxCount:
        res[ind] = maxChar
        ind += 2
        maxCount -= 1
        # print('66',res)
        
    # replace the count of the char with maximum frequency to zero
    # as all the maxChar are already placed in the result
    count[ord(maxChar) - ord('a')] = 0
    # print("70",maxChar)
    # print("70",ord(maxChar))
    # print("72",count[1])

    # print("7111111111",ind)
    # print("755555555",n)

    # place all other char in the result starting from remaining even
    # positions and then place in the odd positions
    for i in range(26):
        while count[i] > 0:
            if ind >= n:
                ind = 1
            # print("833",res)
            # print("844",ind)
            res[ind] = chr(i + ord('a') )
            # print("87",res[ind])
            ind += 2
            print("88",count[i])

            count[i] -= 1
            print("92",count[i])


    # convert the result list to string and return
            # print("89",res)
    return ''.join(res)

# Driver Code
str = 'bbaba'
res = rearrangeString(str)
if res:
    print(res)
else:
    print('Not valid string')

