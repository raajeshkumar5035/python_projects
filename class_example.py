class Al:
    e = int(input("enter e value"))
    f = int(input("enter f value"))

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        c = a + b
        print(c)

    def subtraction(self):
        c = a - b
        print(c)

    @classmethod
    def division(cls):
        c = cls.e / cls.f
        print(c)


a = int(input("enter a value:"))
b = int(input("enter b value:"))

cls1 = Al(a, b)

# cls1.addition()
# cls1.subtraction()
cls1.division()
Al.division()
# Al.subtraction()
