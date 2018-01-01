print("Hello World!\n")

c = 24.21
d = 3


def add_num(a: int, b: int) -> int:
    return a + b


print(str(int(add_num(c, d))) + 'aa')

### Strings
''' aaa.capitalize
' '.replace
' '.isalpha
' '.isdigit
' '.split("'")'''
Str1 = "str name"
Str2 = "str b"
print("hi {0}. I am {1}".format(Str1, Str2))
print((f"hi {Str1}. I am {Str2}"))
print(Str2.replace("s", "a"))
print("\n")

Boo = True
nul = None
# as a placeholder, nontype
if Str1:  # if defined
    print("Yeah")
else:
    print("nah~")

print("bigger" if 2 > 1 else "smaller")
print("\n")

##lists
Lst = ["Item1", "Item2", "ItemLast"]
print(Lst[0])
print(Lst[-1])
print("Item1" in Lst)
print(len(Lst))
Lst.append("AppItem")
print(Lst)
print(Lst[1:])  # slice from index 1 to last
print(Lst[1:-1])  # slice from index 1 to last-1
del Lst[-1]
print(Lst)
print("\n")

# loops
for name in Lst:
    if name == "Item2":
        print("Found")
        continue  # skip printing for Item2
    #    break # break loop if item2 Found
    print("This is {0}".format(name))
print("\n")

x = 0
for index in range(1, 10, 2):  # [0,1,2,3...10] ==> range (from ,to , increment by)
    x += index
    print("This is {0}".format(x))

print("\n")

'''
while x < 10
  x+=1
while True: break
'''

# Dictionaries
student = {
    "name": "Mark",
    "student_id": 1231,
    "feedback": None
}
student["last_name"] = "Lee"
print(student["name"])
print(student.get("name"))
print(student.keys())
print(student.values())

print("\n")
# exceptions
try:
    last_name = student["wrong_name"]
except KeyError as error:  # TypeError, ..., Exception
    print("Error :  " + str(error))

'''
data types
tuple, ~ list, cannot alter
set & frozenset --> only hv unique values
complex
bytes & bytearray


'''
print(set([3, 2, 3, 1, 5]))  # ordered, remove duplicates

