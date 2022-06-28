from asyncore import loop
from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Tracking function: "+func.__name__+"()")
        start=time.time()
        func(*args, **kwargs)
        end=time.time()
        print("Time taken by the function to run is" + str(end -start))
    return wrapper


@timeit
def looper(*args, **kwargs):
    print(f"args={args}")
    print(f"kwargs={kwargs}")

    for loop in kwargs.values():
        for i in range(loop):
            return "Watch looper if you have not | rating=9/10"

looper(2,3,4, loop1=10, loop2=11,loop3=12, loop4=15)
