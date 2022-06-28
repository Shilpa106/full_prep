# Combine two dictionary adding values for common keys
# Input: dict1 = {'a': 12, 'for': 25, 'c': 9}
#        dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}

# Output: {'for': 325, 'Geeks': 100, 'geek': 200}

dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}

# M1.
# for key in dict2:
#     if key in dict1:
#         dict2[key] =dict2[key]+ dict1[key]
#     else:
#         pass

# print(dict2)


# Method #2: Using collections.Counter()
# from collections import Counter
# cdict=Counter(dict1) + Counter(dict2)
# print(cdict)

# Method #3: Using itertools.chain()

# import itertools
# import collections
# cdict=collections.defaultdict(int)
# # print(cdict)
# for key,value in itertools.chain(dict1.items(), dict2.items()): #
#     cdict[key]+=value
# print(dict(cdict))


# Method #4: Using functools.reduce and dict comprehension

from functools import reduce
dict_seq=[{'a': 1, 'b': 2, 'c': 3},
  {'a':10, 'b': 20},
  {'b': 100},]
# print(dict_seq)
print(reduce(lambda d1,d2 :{k:d1.get(k,0)+d2.get(k,0) for k in set(d1)|set(d2)}, dict_seq))




