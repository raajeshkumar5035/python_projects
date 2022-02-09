class First:

    def addition(self, a, b):
        c = a + b
        print(c)


class Second:

    def subtraction(self, a, b):
        c = a - b
        print(c)


class Third(First, Second):               # 'Class Third inherit class First and class Second'

    def multiplication(self, a, b):
        c = a * b
        print(c)


i = int(input("enter i value:"))
j = int(input("enter j value"))

s1 = Third()
s1.addition(i, j)
s1.subtraction(i, j)
s1.multiplication(i, j)
