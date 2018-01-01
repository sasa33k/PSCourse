
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