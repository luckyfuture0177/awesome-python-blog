def triangles(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L = [0]+L+[0]
        L = [L[i]+L[i+1] for i in range(0, len(L)-1)]
        n += 1

for n in triangles(6):
    print(n)


