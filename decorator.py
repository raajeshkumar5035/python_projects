def student_list(name, roll_number):
    print("name of the student:", name)
    print("student roll_number:", roll_number)


def smart_class_student(func):

    def update(xyz, sdf, section):
        print("student section:", section)
        return func(xyz, sdf)       # ' this will call the student_list function'

    return update


student_list = smart_class_student(student_list)

student_list("rajesh", 4, 'A')
