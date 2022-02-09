def add(a, b):              # ' here a and b are called formal arguments
    c = a + b
    print(c)


add(4, 5)    # 'here 4 and 5 are actual arguments'
add(5, 6)    # 'actual arguments are 4 types, position,keyword,default,variable length.here 5 and 6 are position
add(a=8, b=9)    # 'here 8 and 9 are keyword type variables'


def add1(a, b=9):       # 'here b is a default arguments'
    c = a + b
    print(c)


add1(9)


def add2(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)


add2(3, 5, 6, 9)        # 'here the list of values are arguments length type'


def add3(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


add3(4, 5, 6, 101)


def school1(name, **data):
    print(name)
    print(data)                 # 'here is another example for arguments length type arguments'


school1('vhs', sectionname='First', strength=50)


def school1(**data):
    # ' print(name)'
    for i, j in data.items():
        print(i, j)


school1(schoolname='vhs', sectionname='First', strength=50)
