

# # Example 1: Python zip two lists

# name=['Manjeet','Nikhil','shambhavi','astha']
# roll_no=[4,1,3,2]
# mapped = zip(name,roll_no)
# print(set(mapped))

# Example 2: Python zip enumerate

# names = ['Mukesh', 'Roni', 'Chari']
# ages = [24, 50, 18]

# for i, (name,age) in enumerate(zip(names,ages)):
#     print(i, name, age)


# # Example 3: Python zip() Dictionary

# stocks = ['reliance', 'infosys', 'tcs']
# prices = [2175, 1127, 2750]

# new_dict={stocks:prices for stocks,prices in zip(stocks, prices)}
# print(new_dict)


# # How to unzip? 
# name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
# roll_no = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]

# mapped=list(zip(name,roll_no,marks))
# print(mapped)

# # unzipping values
# namez,roll_noz,marksz =zip(*mapped)
# print(namez,roll_noz,marksz)


players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
 
# initializing their scores
scores = [100, 15, 17, 28, 43]
for pl,sc in zip(players,scores):
    print("Player :%s  Score:%d" % (pl,sc))
    