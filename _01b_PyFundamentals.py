'''
special comment on the first line beginning #!
controls module execution by the program loader (The Whole Shebang)
e.g. #!/usr/bin/env python3
terminal: chmod +x words.py
./words.py http://sss.sss
run~!


Python module: Covenient import with API
Python script: Convenient execution from command line
Python program: perhaps coposed of many modules

    (file name)
from words import (fetch_words, print_words)
from words import *

import sys
url = sys.argv[1] # include in the __name__ function, let it expect an argument when being import / run
argv[0] is the sys file name

python3 words http://xxx.xxx.xx   (expected 1 argument)
'''



# Read url text file, each line, split into words and append to story_word list

from urllib.request import urlopen

def fetch_words():
    """ DocStrings
    comment of the function (can be retrieved with :  help(func_name) )
    :return:
    """
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            #line_words = line.split()  # http request by default read raw bytes from network
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    print(story_words)

if __name__ == '__main__':  # __name__ execute once when first import, determine how the module is being used,
                           # evaluates to "__main__" or actual module name..
    fetch_words()
