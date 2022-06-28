
# ***************decorator***********************
import time
import math

def calculate_time(func):
    def inner(*args, **kwargs):
        begin=time.time()
        func(*args, **kwargs)
        end=time.time()
        print("Time taken by :",func.__name__,end-begin)
    return inner
     
@calculate_time
def add(num1,num2):
    print(num1+num2)

add(999,777)

    