# import hs_student   #import the file, need to specify --> hs_student.HighSchoolStudent
from hs_student import HighSchoolStudent  #import the class only, no need to specify hs_student.XXclass anymore
# from hs_student import *  # also work.. but may forgot what have imported..


james = HighSchoolStudent("james")
print(james.get_school_name())
print(james.get_name_capitalize())