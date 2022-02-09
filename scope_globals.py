a = 10
print(id(a))


def someo1():
    a = 9
    print(id(a))
    x = globals()['a']
    print(id(x))
    print("inside", a)
    globals()['a'] = 15
    print("inside fun", a)
    print(id(a))


someo1()
print(a)
print(id(a))
