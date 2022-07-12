# X =[4] * 5
# print(X)

s = 'bbbaa'
count = [0] * 26
for char in s:
    # print(char)
    # print(ord(char))
    # print(ord(char) - ord('a'))
    count[ord(char) - ord('a')] += 1
    print(count)
    # print(count[1])