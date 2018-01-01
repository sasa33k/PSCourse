
students2 = []

class Student2:
    # class attributes
    """
    Class description
    :param student_id integer - optional Student ID
    """
    school_name = "Elementary School"

    def __init__(self, name, last_name, student_id=0):  # instance attributes
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students2.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name()