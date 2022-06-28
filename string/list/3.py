# Convert Delimiter separated list to Number

# Given a String with delimiter separated numbers, concatenate to form integer after removing delimiter.

# Input : test_str = “1@6@7@8”, delim = ‘@’ 
# Output : 1678 
# Explanation : Joined elements after removing delim “@”
# Input : test_str = “1!6!7!8”, delim = ‘!’ 
# Output : 1678 
# Explanation : Joined elements after removing delim “!” 
 
# test_str = "1@6@7@8"
# delim = '@' 

test_str = '1!6!7!8'
delim = '!'
# Output : 1678 
print(test_str)

print(test_str.replace(delim,''))