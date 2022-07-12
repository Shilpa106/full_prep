
import pandas as pd
import numpy as np

# dict={'First Score':[100,90,np.nan,95],
#       'Second Score':[30,45,56,np.nan],
#       'Third Score':[np.nan,40,80,98],
#       'Gender':['male', 'female','','female']}


# # creating a dataframe from list
# df=pd.DataFrame(dict)

# # using isnull() function
# print(df)
# # print(df.isnull())


# # Creating bool series True for NaN values
data=pd.read_csv("./test.csv")
# print(data)
# # Creating bool series True for NaN values
# bool_series=pd.isnull(data['age'])

# # filtering data displaying data only with age=NaN
# print(data[bool_series])


# Checking for missing values using notnull()
import pandas as pd 
# import numpy as np
dict={'First Score':[100,90,np.nan,95],
      'Second Score':[30,45,56,np.nan],
      'Third Score':[np.nan,40,80,98]}

# # Creating a dataframe using dict
df=pd.DataFrame(dict)

# # using notnull() function
# print(df)
# print(df.notnull())


# # ex5
# bool_series=pd.notnull(data['height'])

# # # filtering data displaying data only with age=NaN
# print(data[bool_series])


# print(df)
# print(df.fillna(0))

# 2 filling null values with prev one.
# print(df.fillna(method='pad'))

# 3 filling null values with next one.
# print(df.fillna(method='bfill'))

# print(data)
# print(data[4:8])

# print(data.replace(to_replace=np.nan, value=-99))

# using interpolate() function to fill the missing values using linear method
df2=pd.DataFrame({"A":[12,4,5,None,1],
                  "B":[None,2,54,3,None],
                  "C":[20,16,None,3,8],
                  "D":[14,3,None,None,6]})
# print(df2)
# print(df2.interpolate(method='linear',limit_direction='forward'))


# Dropping missing values using dropna()
dict3 = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df3 = pd.DataFrame(dict3)
   
# print(df3)

# print(df3.dropna())

# Code 2 dropping rows if all values in that row are missing 
dict4={'First Score':[100,np.nan,np.nan,95],
      'Second Score':[30,np.nan,45,56],
      'Third Score':[52,np.nan,80,98],
      'Fourth Score':[np.nan,np.nan,np.nan,65]}
df4=pd.DataFrame(dict4)
# print(df4)
# print(df4.dropna(how='all'))

# code3 dropping columns with at least 1 null value.
dict5={'First Score':[100,np.nan,np.nan,95],
      'Second Score':[30,np.nan,45,56],
      'Third Score':[52,np.nan,80,98],
      'Fourth Score':[60,67,68,65]}
df5=pd.DataFrame(dict5)
print(df5)
# print(df5.dropna(axis=1))
# print(df5.dropna(axis=0,how='any'))



