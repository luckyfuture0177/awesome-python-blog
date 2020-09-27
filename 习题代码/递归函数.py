def move(n,a,b,c):
    if n == 0:
        return 0
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)  # 将a除了最后一块都移动到b上 a上有n块
        move(1,a,b,c)    # 将a的最后一块移动到c上  a上有1块
        move(n-1,b,a,c)  # 将b所有的块移动到c上  b上有n-1块

move(4,'A','B','C')


