"""
unittest
- unit tests
- integration tests
- acceptance tests
--> automated & repeatable tests

TestCase * basic units
fixtures - code run berfore / after each test func, tear-down / cleanup
assertions - specific checks   .is_valid() , == , raise errors

** test_ prefix automatically registered
__main__ search for all tests in the class to run

"""
"""
PDB - Python DeBugger --> module by python

import pdb
pdb.set_trace() # halt execution n back to debugger

ps ax | grep XXX
top -pid XXPIDXX

Ctrl+C to kill prog


python3 -m pdb XX.py
-m: execute module as a script
remaining arg pass into the script

cont
until hit bug : ctrl+C to back to debugger

where
print (var) to check..


(pdb)quit

"""
"""
### venv
python3 -m venv venv_name
source venv_name/bin/activate
deactivate


Packaging
: distutil

# setup.py
----
from distutils.core import setup

setup(
    name='ppp',
    version='1.0',
    py_modules=['ppp']  ## modules to be imported (exclude .py)
    
    # metadata
    author
    author_email
    description
    license
    keywords
)


--------
run
python setup.py install
(copy to the installation folder, site-pakages)
import ppp
ppp.__file__

"""

"""
packaging / source distribution

python setup.py sdist --format zip
python setup.py sdist --help-format (bztar, gztar, tar, zip, ztar)

----
Installing Python with Pip (>=3.4) pip install --upgrade

Central repository: Python Package Index (PyPI) - to install python software

e.g. nose testing tools, no need add unittest class, find all tests
pip install ppp.zip
pip uninstall ppp.zip  # pip advanatage to uninstall



"""

import os
import unittest


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns: A tuple where the first element is the number of lines in
        the file and the second element is the number of characters.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:  # just count line #: return sum(1 for _ in f)
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self): #fixtures
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self): #fixtures
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)  # delete file created in setup
        except:
            pass  # all exception acceptable

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 131)

    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()

