class roman():
    def romanToInt(self,s):
        allowedChars = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0
        for char in s:
            if char in allowedChars:
                ans+=allowedChars[char]


        return ans

c=roman()
print(c.romanToInt('IV'))      