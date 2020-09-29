# 不显示函数名，返回值是表达式的结果
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 200)))

L1 = list(filter(lambda x: x % 2 == 1,range(1, 200) ))

print(L)
print(L1)
