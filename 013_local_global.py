def f():
    print(a)
a = 1
f()

def f():
    a = 1
f()
print(a)

def f():
    a = 1
    print(a, end=' ')
a = 0
f()
print(a)

def f():
    print(a)
    if False:
        a = 0
a = 1
f()

def f():
    global a
    a = 1
    print(a, end=' ')
a = 0
f()
print(a)