import numpy as np
import pandas as pd
from pandas import Series,DataFrame

series_obj=Series(np.arange(8),index=['row1','row2','row3','row4','row5','row6','row7','row8'])

# print(series_obj)
# print(series_obj['row7'])

# print(series_obj[[0,7]])

# print(np.random.seed(25))
print(np.random.rand(36).reshape((6,6)),index=['row1', 'row2','row3','row4','row5','row6'],columns=['column1','column2','column3','column4','column5','column6'])
# df_obj=DataFrame()