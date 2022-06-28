https://www.google.com/search?q=decorator+toward+datascience&oq=decorator+toward+datascience+&aqs=chrome..69i57.8886j0j1&sourceid=chrome&ie=UTF-8

https://towardsdatascience.com/decorators-in-python-9cf8ba95e8e7
https://towardsdatascience.com/python-decorators-in-10-minutes-c8bca1020235
https://towardsdatascience.com/python-decorators-in-10-minutes-c8bca1020235
Logging Documentation: https://docs.python.org/3/howto/logging.html

Timeout Decorator: https://pypi.org/project/timeout-decorator/

Caching Documentation: https://docs.python.org/3/library/functools.html
https://towardsdatascience.com/function-decorators-in-python-a17958b9d618

https://www.google.com/search?q=decorator+toward+datascience&oq=decorator+toward+datascience+&aqs=chrome..69i57.8886j0j1&sourceid=chrome&ie=UTF-8

https://towardsdatascience.com/5-advanced-tips-on-python-decorators-113307d5a92c



import time
from itertools import izip
from random import shuffle

def timing_val(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper

@timing_val
def time_izip(alist, n):
    i = iter(alist)
    return [x for x in izip(*[i] * n)]

@timing_val
def time_indexing(alist, n):
    return [alist[i:i + n] for i in range(0, len(alist), n)]

func_list = [locals()[key] for key in locals().keys()
             if callable(locals()[key]) and key.startswith('time')]
shuffle(func_list)  # Shuffle, just in case the order matters

alist = range(1000000)
times = []
for f in func_list:
    times.append(f(alist, 31))

times.sort(key=lambda x: x[0])
for (time, result, func_name) in times:
    print(time*1000)
    # print '%s took %0.3fms.' % (func_name, time * 1000)