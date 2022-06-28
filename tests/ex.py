# aaaabbbcccddeea  out='a4b3c3d2e2a1'



# ["shipa is good girl","ram is bad boy"]

# ex=["shipa is good girl","ram is bad boy"]
# count=0
# for i in ex:
#     if 'is' in i:
#         count+=1
# print(count)



# "abc"

# aaaabbbcccddeea  out='a4b3c3d2e2a1'


# # *****
# n=3
# s = ""
# for i in range(n):
#     s+=str(i)
# print(s)
# # *****

def solve(s):
   result = ""
   cnt = 1
   for i in range(1, len(s)):
      if s[i - 1] == s[i]:
          cnt += 1
      else:
         result = result + s[i - 1]
         print("37",result)

        
         if cnt >= 1:
            result += str(cnt)
            print("42",result)
         cnt = 1
   result = result + s[i]
   print("45",result)
   if cnt >= 1:
      result += str(cnt)
      print("48",result)
    
   return result

s = "aamaabbbcccddeea"
print(solve(s))
  

# p='abc'
