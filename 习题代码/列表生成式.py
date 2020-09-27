L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() if isinstance(s,str) else continue for s in L1]
L3 = [s.lower() for s in L1 if isinstance(s,str)]
print(L3)
L2 = [x if x % 2 == 0 else -x for x in range(1, 11)]
