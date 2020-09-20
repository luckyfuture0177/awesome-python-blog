import itertools

# 计算圆周率值
def pi(N):
    odd_list = itertools.count(1, 2)
    odd = itertools.takewhile(lambda x: x <= (2 * N - 1), odd_list)
    odd = list(odd)
    for i in range(1, N + 1):
        if i % 2 == 1:
            odd[i - 1] = 4 / odd[i - 1]
        else:
            odd[i - 1] = 0 - 4 / odd[i - 1]
    return sum(odd)
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


