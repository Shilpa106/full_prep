# Find duplicate rows in a Dataframe based on all or selected columns

# For this, we will use Dataframe.duplicated() method of Pandas.
 

# Syntax : DataFrame.duplicated(subset = None, keep = ‘first’)
# Parameters: 
# subset: This Takes a column or list of column label. It’s default value is None. After passing columns, it will consider them only for duplicates.
# keep: This Controls how to consider duplicate value. It has only three distinct value and default is ‘first’. 


# If ‘first’, This considers first value as unique and rest of the same values as duplicate.
# If ‘last’, This considers last value as unique and rest of the same values as duplicate.
# If ‘False’, This considers all of the same values as duplicates.
# Returns: Boolean Series denoting duplicate rows. 
 