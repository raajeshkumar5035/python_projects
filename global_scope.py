a = 6


def globe_scope():
    global a
    a = 13
    print("in the function scope:", a)


globe_scope()
print("outside of the function:", a)
