"""
REPL : read evaluate print & loop

Strong type system: there is no implicit type conversion (except bool)
Dynamic type system: object types are only resolved at runtime

Scopes: contexts in which named references can be looked up
Local (current function), enclosing,  Global (top-level), Built-in
Python named scopes : LEGB

type()
dir()
words.fetch_words.__name__  ==> fetch_words
words.fetch_words.__doc__  ==> comment in docstring

x = 5
x
3*x
_*2 # evaluated values

prefer 4 spaces indented
comment 2 space # space XXX

import math
help(math)
from math import factorial as fac  # rename the function name.. for simplicity
/ # floating point divisor
// # integer divisor
2**31 - 1 # signed integer maximum in other programing language 2 to the power 31
# python limit only by memory of computer
len(str(fac(n)))

int(-3.5) # rounding towards zero ==> -3
int("10000",3)  # base 3 ==> 81

3e8 ==> 300000000.0

nan, inf # not a num / infinity

a = None
a is None ==> True

bool(0) ==> False
bool([]) ==> False

== != < > <= >=
-= +=

elif (else if)

control + D ==> exit the REPL
ctrl+Z on windows

ctrl-C interrupt execution to create a KeyboardInterrupt execution


"""

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
# back slash escape \\
# raw string (what u see wt u get) : r'path\fs\f'
# str encode to bytes decode to str ... d = b'some bytes'
# BYTE = data.encode('utf-8')
# STR = BYTE.decode('utf-8')
# STR = data
print('a\\b')
print(r'a\b')

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
"""
list("char")
['c', 'h', 'a', 'r']
"""




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

while True:
    response = input()
    print(int(response))
    if int(response) % 7 == 0:
        break

# Dictionaries
# dictionaries, mutable mapping of keys to values

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


"""
id

variable a=100
create an integer object 100, "a" pointing name reference to it
id(a)
b = [1,2,3]
s = b
pointing s reference to b
change s[0]=10, b also being changed

test:
b is s  # identity : same object
b == s  # value equals



"""


def banner(message, border='-'):
    line = border * len(message)  # repetition of string
    print(line)
    print(message)
    print(line)

banner("la la la", "*")

# default argument values are evaluated when def is evaluated
import time
time.ctime()
def show_default(arg=time.ctime()):
    print(arg)


def add_spam(menu=[]):  # WRONG~! keep appending when it is being called
    menu.append('spam')
    return menu

def add_spam2(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu