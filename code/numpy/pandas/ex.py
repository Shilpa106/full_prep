import pandas as pd
# Creating an empty dataframe
# df=pd.DataFrame()
# print(df)

# Creating a dataframe using list
# lst=['geeks','for','geeks','is','portal','for','geeks']
# df=pd.DataFrame(lst)
# print(df)

# # Creating DataFrame from dict of ndarray/lists:
# data={'Name':['Tom','nick','krish','jack'],'Age':[20,21,19,18]}

# # Create DataFrame
# df=pd.DataFrame(data)
# print(df)

# Create pandas dataframe from lists using dictionary:
# import pandas as pd
# dict={'name':["aparna","pankaj","sudhir","Geeku"],'degree':["MBA","BCA","M.Tech","MBA"],'score':[90,40,80,98]}
# df=pd.DataFrame(dict)
# print(df)

# # Different ways to create Pandas Dataframe/
# import pandas as pd
# data=[10,20,30,40,50,60]
# # create the pandas dataframe with column name is provided explicitly
# df=pd.DataFrame(data,columns=['Numbers'])
# print(df)


# # Creating pandas dataframe from list of lists
# # print(data)
# data=[['tom',10],['nick',15],['juli',14]]
# df=pd.DataFrame(data, columns=['Name','Age'])
# # df=pd.DataFrame(data)
# print(df)

# # Creating a DataFrame by providing index label explicitly
# data={'Name':['Tom','Jack','nick','juli'],'marks':[99,98,95,90]}

# # Creates pandas DataFrame.
# df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
# print(df)

# # Creating DataFrame from lists of dicts.
# data=[{'a':1,'b':2,'c':3},{'a':10,'b':20,'c':30}]
# df=pd.DataFrame(data)
# print(df)


# data=[{'b':2,'c':3},{'a':10,'b':20,'c':30}]

# # Creates pandas DataFrame by passing lists of dictionary
# # and row index
# df=pd.DataFrame(data, index=['first','second'])
# print(df)

# data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
# df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])

# # with two column indices with one index with other name
# df2=pd.DataFrame(data, index=['first','second'],columns=['a','b1'])
# # print(df1)
# print(df2)

# # Creating DataFrame using zip functions
# Name=['tom','krish','nick','juli']
# Age=[25,30,26,22]
# list_of_tuples=list(zip(Name,Age))
# print(list_of_tuples)

# df=pd.DataFrame(list_of_tuples,columns=['Name','Age'])
# print(df)

# # Creating DataFrame from series
# d=pd.Series([10,20,30,40])
# # Creates DataFrame
# # print(d)
# df=pd.DataFrame(d)
# print(df)

# creating DataFrame from Dictionary of series
d={'one':pd.Series([10,20,30,40],index=['a','b','c','d']),
   'two':pd.Series([10,20,30,40],index=['a','b','c','l'])}

df=pd.DataFrame(d)
print(df)

