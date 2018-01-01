students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=0):
    student = {"name": name, "student_id": student_id}
    students.append(student)


# READ / WRITE FILES
def save_file(student):
    try:
        f = open("students.txt",
                 "a")  # access mode: w-overwrite entire file, r-reading a text file, a-appending, rb-reading a binary file, wb - writing to a binary file
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():  # replace f.readlines with read_students(f)
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# GENERATOR function, every time yield a single line, continue for all lines
def read_students(f):
    for line in f:
        yield line

    # LAMBDA functions @ higher order functions, take function as argument, e.g. filter function


double = lambda x: x * 2


def double(x):
    return x * 2


# add_student("Mark",332)
student_list = get_students_titlecase()

read_file()
print_students_titlecase()

student_name = input("Enter student name: ")
student_id = input("Enter student ID:")

add_student(student_name, student_id)
save_file(student_name)


def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):  # keyword arguments
    print(name)
    print(kwargs["description"], kwargs["feedback"])


var_kwargs("Mark", description="desc", feedback=None, Sub=True)