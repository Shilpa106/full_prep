
import numpy as np
my_vector=np.array([-17,-4,0,2,21,37,105])
mod_test=0==(my_vector%7)
# print(mod_test)
positive_test=my_vector>0
# print(positive_test)

combined_mask=np.logical_and (mod_test,positive_test)
# print(combined_mask)

# print(my_vector[combined_mask])