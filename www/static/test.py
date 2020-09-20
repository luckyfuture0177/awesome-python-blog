x = 2

def f():
    print(x)

def g():
    print(x)

def h():
    print(x)
    exec('x = 3')

try: f()
except: print('Oops')
try: g()
except: print('Oops')
try: h()
except: print('Oops')