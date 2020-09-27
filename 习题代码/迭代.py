def findMinAndMax(L):
    if (not L):
        return None,None
    min = L[0]
    max = L[0]
    for l in L:
        if l<min:
            min = l
        if l>max:
            max = l
    return min,max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')