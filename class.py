# class Student:
#     name = ""
#     roll = 0


# student1 = Student()
# student1.name = "Ratul"
# student1.roll = 1

# print(student1.name)


class Student:
    def __init__(self, name_inpput, roll_input, mark_input):
        self.name = name_inpput
        self.roll = roll_input
        self.marks = mark_input

student1 = Student("Jubayer", 1, 98)
student2 = Student("Ahmed", 1, 82)

print(student1.name)
print(student2.name)


    