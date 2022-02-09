class First:

    def addition(self, a, b):
        c = a + b
        print(c)


class Second(First):                # 'class Second inherit class First'

    def subtraction(self, a, b):
        c = a - b
        print(c)


class Third(Second):               # 'Class Third inherit class Second'

    def multiplication(self, a, b):
        c = a * b
        print(c)


i = int(input("enter i value:"))
j = int(input("enter j value"))

s1 = Third()
s1.addition(i, j)
s1.subtraction(i, j)
s1.multiplication(i, j)
