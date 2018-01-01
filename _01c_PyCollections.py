"""
tuple
str
range
list
dict
set

"""
#Tuple:  immutable, can be nested, usefull for multiple return values
t=("Nor",1.2,3)
t[0]
t + (4,6)
t*3 #repeat
#cannot use one object in () as a single element tuple, have to include a trailing comma
k=(123,)
type(k)

def minmax(items):
    return min(items), max(items)

minmax([1,4,6,8,2])
lower,upper = minmax([1,4,6,8,2]) # tuple unpacking - destructure directly into named reference
print(lower)
print(upper)

tuple("hello")
('h', 'e', 'l', 'l', 'o')
tuple([1,3,2])
# in or not in
1 in tuple([1,3,2]) #True


###


#str
len("abc")
"ab" + "c"
txt = ';'.join(['ab','c']) #join on separator string
txt.split(';')
'unforgetable'.partition('forget') #('un', 'forget', 'able')
a,_,b = "a:b".partition(':')  # _ dummy values

"The {0} of {1}".format('a','b') #'The a of b'
"The {} of {}".format('a','b') #'The a of b'
"The {aa} of {bb}".format(aa='a',bb='b') #'The a of b'
pos = (1.1,2.2,3.3)
"position {pos[0]},{pos[1]},{pos[2]}".format(pos=pos)

import math
"Math constants: pi={m.pi:.3f}, e={m.e}".format(m=math)  #3 d.p.




###

#range
range(5) # range(0, 5)
for i in range(5): #0,1,2,3,4
    print(i)

list(range(0,10,2)) #step:2 [0, 2, 4, 6, 8]

# enumerate
t=['a','b','c']
for p in enumerate(t): # yields (index,value) tuples (0, 'a') (1, 'b') (2, 'c')
    print(p)

for i,v in enumerate(t): #i = 0, v = a  ;  i = 1, v = b  ;  i = 2, v = c
    print("i = {}, v = {}".format(i,v))


####

#List

lst="show me how to do this".split() # ['show', 'me', 'how', 'to', 'do', 'this']
lst[2] #how (starts from 0)
lst[-2] #do (-ve starts from -1)
#search in list
lst.index('how') # 2
'how' in lst # true  vs not in
lst.count('how') # 1
#slice
lst[1:-1] #['me', 'how', 'to', 'do']
#s[:x]+ s[x:] == s

# copying lists (new reference) - shallow copy, create a new list,
# contain the same object ref (if inner list modified, both modified), but dun copy the refered to object
full_slice = lst[:]
u = lst.copy()
v = list(lst) # list constructor

s=[[-1,1]]*5 # repeats 5 times, inner list ref same object.. once modified, modify all
s[3].append(7) # vs del s[3][2] vs s[3].remove(7) ~ del u[u.index('a')]
s  # [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]

a = "I am good".split()  # ['I', 'am', 'good']
a.insert(2,"not")  # ['I', 'am', 'not', 'good']
' '.join(a)  # 'I am not good'

m = [1,2,3]
m += [11,12,13]  # [1, 2, 3, 11, 12, 13]
m.extend([21,22])  # [1, 2, 3, 11, 12, 13, 21, 22]

m.reverse()  # [22, 21, 22, 21, 13, 12, 11, 3, 2, 1]
m.sort()  # [1, 2, 3, 11, 12, 13, 21, 21, 22, 22] vs reverse=True
lst.sort(key=len) # key accepts a function for producing a sort key from an item
# ['me', 'to', 'do', 'how', 'show', 'this']
# sorted() built-in function sorts any interable series and returns a list
# reversed() built-in function reverses any iterable series
k=list(reversed(m))  # [22, 22, 21, 21, 13, 12, 11, 3, 2, 1]



# expr(item for item in iterable
words = "how old are you".split()  # ['how', 'old', 'are', 'you']
[len(word) for word in words]  # [3, 3, 3, 3]
"""
lengths = []
for word in words:
    lengths.append(len(word))

lengths
"""


###

#dict - {} key-value pairs comma separated, keys must be unique, don't rely on its order
# accessible by keys (must be immutable), dict itself, and values (e.g. list) may be mutable
urls={'google': 'google.com',
      'git': 'git.com'}
urls['git']
#dict() constructor accepts iterable series of key-value 2-tuples OR keyword arguements @ valid python arg
d = dict([('goo','goo.com'),('go','go.com')])  # {'goo': 'goo.com', 'go': 'go.com'}
d = dict(goo='goo.com',go='go.com')  # {'goo': 'goo.com', 'go': 'go.com'}
# copying dictionaries
d2 = d.copy()
d2 = dict(d)
f.update(g) # update dict f to include dict in g

colors = dict(aqua='#7FFFD4', maroon='#B03060')
for key in colors: #iteration over keys, get corresponding value with d[key] lookup
    print("{key} => {value}".format(key=key, value=colors[key]))

for value in colors.values(): # no efficient way to get the key corresponding to a value, also can use ".keys()"
    print(value)

for key,value in colors.items():
    print("{key} => {value}".format(key=key, value=value))

#pretty print by using pprint
from pprint import pprint as pp
pp(colors)

country_to_capital={'UK':'London', 'Brazil':'Brazilia'}
capital_to_country = {capital: country for country, capital in country_to_capital.items()} # {'London': 'UK', 'Brazilia': 'Brazil'}
# key_expr:value_expr for item in iterable

words = ["hi","hello","foxtrot","hotel"]
# x[0] : h,h,f,h --> h,f only
{x[0]:x for x in words} # {'h':'hotel', 'f':'foxtrot'}
# Duplicates: later keys overwrite earlier keys

"""
import os
implort glob
file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}
"""
###
# set - unordered collection of unique, immutable objects, duplicates are discarded, not order preserving, iterable
st={6,28,999}
#empty: use set() constructor
st=()

t=[1,4,3,2,1,1,1]
k=set(t) # {1, 2, 3, 4}
k.add(12)  # {1, 2, 3, 4, 12}
k.update([12,24])  # {1, 2, 3, 4, 12, 24} for multiple items to add
#remove(item) requiers item is present, else raises KeyError, discard(item) always succeeds


#Set operations
blond_hair = {'harry','jack'}
o_blood = {'harry','amy'}
a_blood = {'jack'}
ab_blood={'bob'}
blond_hair.union(o_blood) #{'jack', 'amy', 'harry'} either or
blond_hair.intersection(o_blood)  #both {'harry'}
blond_hair.difference(o_blood) # have blond_hair but NOT o_blood{'jack'}
blond_hair.symmetric_difference(o_blood) # either one only {'jack', 'amy'}
a_blood.issubset(blond_hair)  # True
blond_hair.issuperset(a_blood)  # True
ab_blood.isdisjoint(blond_hair)  # True


"""
container (in)  : str, list, range, tuple, bytes, set, dict
sized (len)     : str, list, range, tuple, bytes, set, dict
iterable        : str, list, range, tuple, bytes, set, dict
sequence        : str, list, range, tuple, bytes
(retreive by index[], find items by value .index(item), .count(item), reversed(seq))
Mutable sequence:   list
Mutable Set:        set
Mutable Mapping:    dict

"""


### check prime number iteration
from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

[x for x in range(11) if is_prime(x)]   # [2, 3, 5, 7]

prime_square_divisors = {x*x:(1,x,x*x) for x in range(11)}
#{0: (1, 0, 0), 1: (1, 1, 1), 4: (1, 2, 4), 9: (1, 3, 9), 16: (1, 4, 16), 25: (1, 5, 25), 36: (1, 6, 36), 49: (1, 7, 49), 64: (1, 8, 64), 81: (1, 9, 81), 100: (1, 10, 100)}




"""
Iterable protobol
inter()  # to get an iterator

Iterator protocol
next() to fetch the next item
next()  # to fetch the next item
"""
iterable = ['Spring','Summer','Autumn','Winter']
iterator = iter(iterable)
next(iterator)
next(iterator)
next(iterator)
next(iterator)
#StopIteration

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

