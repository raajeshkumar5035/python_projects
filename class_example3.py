class Al:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def addition():
        c = a + b
        print(c)

    @staticmethod
    def subtraction():
        c = a - b
        print(c)

    @classmethod
    def division(cls):
        c = cls.a / cls.b
        print(c)


a = int(input("enter a value:"))
b = int(input("enter b value:"))

cls1 = Al(a, b)

cls1.addition()
cls1.subtraction()
cls1.division()
Al.division()
# Al.subtraction()
