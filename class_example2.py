class Students:
    section = 9          # ' here section is class variable and class variables also called static variable'

    def __init__(self):
        self.name = "rajesh"            # 'name and roll_number are instance variables'
        self.roll_number = 18


c1 = Students()
c2 = Students()
c2.name = input("enter a name:")
c2.roll_number = int(input("enter roll_number:"))
Students.section = 10               # 'here section is changed it will be changed to all objects'

print(c1.name, c1.roll_number, Students.section)
print(c2.name, c2.roll_number, Students.section)
