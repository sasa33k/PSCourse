from student import Student2



class HighSchoolStudent(Student2):  # derived class
    school_name = "High School"
    def get_school_name(self):
        return "This is High School"
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"