
# Dictionary and counter in python to find winner of election.
from collections import Counter

def winner(input):
    votes=Counter(input)
    # print("votes",votes)
    # print(type(votes))
    dict={}

    for value in votes.values():
        # print("value",value)
        dict[value]=[]
        # print("dict value",dict[value])

    for (key, value) in votes.items():
        # print("key value",key, value, end='')
        dict[value].append(key)
    # print("dict value",dict)

    maxVote=sorted(dict.keys(), reverse=True)[0]
    # print("maxVote",maxVote)
    
    # print(dict[maxVote])
    if len(dict[maxVote])>1:
        print(sorted(dict[maxVote])[0])
    else:
        print(dict[maxVote][0])

if __name__ == "__main__":
    input=['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
    winner(input)
