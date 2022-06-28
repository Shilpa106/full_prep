

# def shout(text):
#     return text.upper() 

# def whisper(text):
#     return text.lower()

# def test(func):
#     greeting=func("hello geeks for geeksSFDF")
#     print(greeting)

# test(shout)
# test(whisper)


# 2.
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder

# add_15=create_adder(12)
# print(add_15(23))

# 3
# def hello_decorator(func):
#     def inner1():
#         print('hello this is before function execution')

#         func()
#         print('this is after function execution')

#     return inner1

# def function_to_be_used():
#     print('this is inside the function')
    
# function_to_be_used=hello_decorator(function_to_be_used)

# function_to_be_used()

# 4

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
    
	def inner():
        
		x = func()
        
		return 2 * x
        
	return inner

@decor1
@decor
def num():
	return 10

print(num())


# # 5
# # execution time of a function

# import time
# import math

# # decorator to calculate duration taken by any function
# def calculate_time(func):
#     def inner1(*args,**kwargs):
#         begin=time.time()
#         func(*args,**kwargs)
#         end=time.time()
#         print("total time taken in : ",func.__name__,end-begin)
#     return inner1

# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

import time
import math

def calculate_time(func):
	def inner(*args, **kwargs):
		begin=time.time()
		func(*args, **kwargs)
		end=time.time()
		print("time taken by",func.__name__ ,end-begin)
	return inner

@calculate_time
def factorial(num):
	time.sleep(2)
	print(math.factorial(num))
factorial(10)
 