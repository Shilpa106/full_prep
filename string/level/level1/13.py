# Generating distinct subsequences of a given string in lexicographic order
# https://www.geeksforgeeks.org/generating-distinct-subsequences-of-a-given-string-in-lexicographic-order/
# Difficulty Level : Hard
# Last Updated : 18 May, 2021
# Given a string s, make a list of all possible combinations of letters of a given string S. If there are two strings with the same set of characters, print the lexicographically smallest arrangement of the two strings
# For string abc, the list in lexicographic order subsequences are, a ab abc ac b bc c
# Examples: 
 

# Input : s = "ab"
# Output : a ab b

# Input  : xyzx
# Output : x xx xy xyx xyz xyzx xz xzx y
#          yx yz yzx z zx
 

# Finds and stores result in st for a given string s
def generate(st,s):
    if len(s) == 0:
        return 

    # if current string is not already present
    if s not in st:
        st.add(s)

        # Traverse current string one by one remove every character and recur.
        for i in range(len(s)):
            # print(s)
            # print(list(s))
            t=list(s).copy()
            t.remove(s[i])
            t=''.join(t)
            print("ttttttttt",t)
            generate(st,t)
    return

# Driver code

if __name__ == '__main__':
    s='gfg'
    st=set()
    generate(st, s)
    for i in st:
        pass
        # print(i)
