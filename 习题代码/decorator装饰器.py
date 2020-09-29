from datetime import datetime
import time
import functools
def metric(func):
    t1 = time.time()
    def wrapper(*args, **kw):
        print('%s executed in ' % func.__name__, end='')
        return func(*args, **kw)
    t2 = time.time()
    print(t2-t1)
    return wrapper

@metric
def fast(x, y):
    time.sleep(1)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(2)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)