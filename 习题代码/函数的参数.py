def product(x, y, *num):
    if(not num):
        return x*y
    else:
        sum = x*y
        for n in num:
            sum = sum*n
        return sum
s = (2,5)
print(product(5,6,*s))
print(product(5,6,2,5))
