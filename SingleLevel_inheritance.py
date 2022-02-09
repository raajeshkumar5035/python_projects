class First:

    def addition(self, a, b):
        c = a + b
        print(c)


class Second(First):

    def subtraction(self, a, b):
        c = a - b
        print(c)


i = int(input("enter i value:"))
j = int(input("enter j value"))

s1 = Second()
s1.addition(i, j)
s1.subtraction(i, j)
