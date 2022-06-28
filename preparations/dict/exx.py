from collections import Counter
  
# initializing dictionary
test_dict = {'Manjeet' : [1, 4, 5, 6],
            'Akash' : [1, 8, 9],
            'Nikhil': [10, 22, 4],
            'Akshat': [5, 11, 22]}
  
# printing original dictionary
print("The original dictionary : " + str(test_dict))
  
# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
cnt = Counter()

# print(test_dict.values())
for idx in test_dict.values():
    print(idx)
    cnt.update(idx)

print(cnt)
res = {idx: [key for key in j if cnt[key] == 1] 
               for idx, j in test_dict.items()}
  
# printing result 
print("Uncommon elements records : " + str(res)) 


# **************************************************



