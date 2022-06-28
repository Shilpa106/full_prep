# Filter immutable rows representing Dictionary Keys from Matrix
# Input : test_list = [[4, 5, [2, 3, 2]], [“gfg”, 1, (4, 4)], [{5:4}, 3, “good”], [True, “best”]] 
# Output : [[‘gfg’, 1, (4, 4)], [True, ‘best’]] 
# Explanation : All elements in tuples are immutable.
 

# Input : test_list = [[4, 5, [2, 3, 2]], [“gfg”, 1, (4, 4), [3, 2]], [{5:4}, 3, “good”], [True, “best”]] 
# Output : [[True, ‘best’]] 
# Explanation : All elements in tuples are immutable. 

