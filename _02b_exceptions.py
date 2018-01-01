"""
raise an exception to interrupt program flow
handle an exception to resume control
unhandled exception will terminate the program
exception objects contain info about the exception event


"""

def convert(s):
    try:
        x = int(s)
        print(x)
    except ValueError:
        print("Cannot convert (str)")
        x = -1
    except TypeError:
        print("Cannot convert (list)")
        x = -1
    return x

def convert2(s):
    x = -1
    try:
        x = int(s)
        print(x)
    except (TypeError, ValueError):
        print("Cannot convert") # need "pass" if removed, else have indentation error
    return x

"""
Exceptions for programmer errors
IndentationError
SyntaxError
NameError
"""

import sys

def convert3(s):
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion error: {}"\
              .format(str(e)),
              file=sys.stderr)
        return -1
    # Conversion error: invalid literal for int() with base 10: 'aa'
    # -1


def convert3(s):
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion error: {}"\
              .format(str(e)),
              file=sys.stderr)
        raise  # re-raise the error?
"""
Conversion error: invalid literal for int() with base 10: 'aa'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 3, in convert3
ValueError: invalid literal for int() with base 10: 'aa'
"""


"""
exception, break the program and will not continue for the next line

ValueError:
1. (wasteful~)
except ZeroDivisionError:
   raise ValueError()
   
2. 
if x < 0:
  raise ValueError("Cannot compute square root of negative number {}".format(x))

except ValueError as e:
  print(e, file=sys.stderr)

"""

"""
Use common or existing exception types when possible
IndexError - integer index is out of range e.g. z[4] but z only hv 2 elements
KeyError - lookup in a mapping fails e.g. code = dict(a=1,b=2) ==> codes['d'] ==> KeyError
ValueError - object is of the right type, but inappropriate value e.g. int("aa")
TypeError ** avoid protecting against type errors --> aginst the grain in Python, limit reuse potential uneccessarily
...

"""

"""
Handling failure
1. Look Before You Leap - LBYL
    e.g.
    import os
    p = '/path/to/file.dat'
    
    if os.path.exists(p):   # check only existance.. what if gabbage/directory?, race condition (delete by other process in between exist and process_file)
        process_file(p)
    else:
        print('no such file')
        
2. *It's Easier to Ask Forgiveness than Permission - EAFP ** Exceptions handling
    e.g.
    import os
    p = '/path/to/file.dat'
    
    try
        process_file(p)
    except OSError as e:
        print('Could not process file because()'\
                .format(str(e)))
            
"""
"""
#clean up

import os
def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    os.mkdir(dir_name)  # if this fails, next line won't happen
    os.chdir(original_path)
    
    
VS

import os
def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)  
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path) # do this even above fails

"""
"""
Platform specific code
Windows 
- try: import msvcrt 
- msvcrt.getch() #wait for a keypress and return a single character string

OSX or Linux
- sys, tty, termios

"""

"""keypress - A module for detecting a single keypress."""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character string."""
        return msvcrt.getch()

except ImportError:  # because not windows

    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

    # If either of the Unix-specific tty or termios are not found,
    # we allow the ImportError to propagate from here

