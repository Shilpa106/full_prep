# Sort Dictionary by Values and Keys

# Input : test_dict = {'gfg' : 1, 'is' : 1, 'best' : 1, 'for' : 1, 'geeks' : 1}
# Output : {'best' : 1, 'is' : 1, 'for' : 1, 'geeks' : 1, 'gfg' : 1}
# Explanation : All values are equal, hence lexicographically sorted keys.

# Input : test_dict = {'gfg' : 5, 'is' : 4, 'best' : 3, 'for' : 2, 'geeks' : 1}
# Output : {'gfg' : 5, 'is' : 4, 'best' : 3, 'for' : 2, 'geeks' : 1}
# Explanation : All values are different, hence descending ordered sorted.

# Method : Using sorted() + items() + dictionary comprehension + lambda
test_dict = {'gfg' : 5, 'is' : 4, 'best' : 9, 'for' : 2, 'geeks' : 1}
res={val[0] : val[1] for val in sorted(test_dict.items(),key=lambda x:(-x[1],x[0]))}
# res={val[0] : val[1] for val in sorted(test_dict.items(),key=lambda x:(-x[1],x[0]))}
print(res)