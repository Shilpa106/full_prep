import pandas as pd
nba=pd.read_csv("./test.csv")
# df = pd.read_excel("D:\\selenium\\asosproject\\asoscat.xlsx")
print(nba)

# # After replacing null values
# print("after replacing null values")
# nba["college"].fillna("no college",inplace=True)
# nba['weight'].fillna("under weight", inplace=True)
# nba['height'].fillna("overheight",inplace=True)
# print(nba)


# nba['college'].fillna(method='ffill',inplace=True)
# nba['college'].fillna(method='bfill',inplace=True)
# nba['college'].fillna(method='backfill',inplace=True)
# print(nba)

nba['college'].fillna(method='ffill',limit=1,inplace=True)
print(nba)


# Example #3: Using Limit
