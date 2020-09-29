from datetime import datetime
import time
def metric(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        func(*args, **kw)
        t2 = time.time()
        print('%s executed in ' % func.__name__, end='')
        print(t2 - t1)
        return func(*args, **kw)
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
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')