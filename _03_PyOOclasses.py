# Class - logical group of functions (method) & data *readable & maintainable *special methods only available in class e.g. constructor method

students = []


class Student:
    def __init__(self, name, student_id=0):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def add_student(self, name, student_id=0):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    # pass #do nothing

    def __str__(self):  # overwrite--> print(mark): instead of address, print the word "Student"
        return "Student"


'''
student = Student() #create a new instance of Student class Cap @ clasess, var & function @ small letters
student.add_student("Mark")
'''
mark = Student("Marky")
print(students)

print(mark)

####
students2 = []


class Student2:
    # class attributes
    school_name = "Elementary School"

    def __init__(self, name, student_id=0):  # instance attributes
        self.name = name
        self.student_id = student_id
        students2.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name()


mark2 = Student2("Marky")
print(mark2)
# print(mark2.get_school_name)
print(Student2.school_name)


class HighSchoolStudent(Student2):  # derived class
    school_name = "High School"
    def get_school_name(self):
        return "This is High School"
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

james = HighSchoolStudent("james")
print(james.get_school_name())
print(james.get_name_capitalize())









