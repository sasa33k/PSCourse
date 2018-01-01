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



"""
Generators in Python (use "yield" at least once)
- iterators, laxily evaluated ("next" on demand), can model infinite sequence, are composable into pipelines (for natural stream processing)
"""
def gen123():
    yield 3
    yield 2
    yield 4

g = gen123()
next(g)  # 3
next(g)  # 2

for v in gen123():
    print(v)

"""
Stateful generators - complex control flow, lazy evaluation
e.g. get first 3 unique numbers --> exit once found
"""
(x*x for x in range (1,101))  # generator, use once only
list(x*x for x in range (1,101))
sum(x*x for x in range (1,101))  # no need additional ()

# sum(x*x for x in range (1,101) if is_prime(x))  ]

any([False, False, True])
all([False, False, True])

#zip in tuples
sun = [1,2]
mon = [3,4]

for item in zip(sun,mon):
    print(item)

"""
(1, 3)
(2, 4)
"""
for sun,mon in zip(sun,mon):
    print((sun+mon)/2)
    #chain

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