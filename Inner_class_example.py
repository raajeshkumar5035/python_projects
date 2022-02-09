class Students:

    def __init__(self, name):
        self.name = name
        self.age = input("enter age:")
        # 'self.Rolling = self.Rolling()'           # 'either ways we can create the inner class object'

    def show(self):
        print("student name is:", self.name)
        print("student age is:", self.age)
        # 'self.Rolling.show()'                     # 'either ways we can call the inner class method'

    class Rolling:

        def __init__(self):
            self.number = input("enter roll number:")

        def show(self):
            print("student roll number:", self.number)


student = input("enter a name:")
s1 = Students(student)
s1.show()
s2 = Students.Rolling()                 # 'either ways we can create object of the inner class'
s2.show()                               # 'either ways we can call the inner class method'
