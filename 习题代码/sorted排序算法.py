L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(L):
    t = []
    for valus in L:
        t.append(valus[0].lower())
    return t

L2 = sorted(L, key=by_name)
print(L2)

