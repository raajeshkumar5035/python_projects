# 'this is duck type polymorphism'
class First:
    def addition(self, a, b):
        c = a + b
        print(c)
        print("this is first class")


class Third:
    def addition(self, a, b):
        c = a - b
        print(c)
        print("this is third class")


class Second:
    def subtraction(self, ide):
        print("this is second class")
        ide.addition(a, b)


a = int(input("enter a value:"))
b = int(input("enter b value:"))
ide = Third()
sec = Second()
sec.subtraction(ide)
