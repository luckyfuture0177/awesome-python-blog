import math

def quadratic(a,b,c):
    if(pow(b,2)-4*a*c<0):
        return '此题无解'
    else:
        x1 = ((0-b) + math.sqrt(pow(b, 2)-4*a*c))/(2*a)
        x2 = ((0-b) - math.sqrt(pow(b, 2)-4*a*c))/(2*a)
        return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')