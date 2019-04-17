#!/usr/bin/env python3

"""
Application - The way to make things right.
Usage:
  application.py arg1 [--arg2 <key>]
  application.py (-h | --help)
  application.py --version
Options:
  -h, --help    Show this screen.
  --version     Show version.
  --arg2 <key>  Another argument [default: 42].
"""

from learning.API.exampleAPI import SomeClass

# INFO

__author__ = 'Amrith h namboodiri'
__copyright__ = 'Copyright 2019, project name '
__credits__ = ["Amrith h namboodiri"]
__license__ = 'GPL'
__version__ = "0.1.0"
__date__ = '19-3-2019'
__maintainer__ = "Amrith h namboodiri"
__email__ = "amrithmmh@gmail.com"
__status__ = "Development"
__description__ = 'My First Project Program.'

class NewClass:
    """CLASS DOCSTRING"""
    def __init__(self):
        print("inside {}".format(self.__class__.__name__))
        self.name = "abc"

    def func(self):
        """func"""
        self.name = "hello"
        print("inside func")

    def func2(self):
        """func"""
        self.name = "hello"
        print("inside func2")

def function():
    """FUNCTION DOCSTRING"""
    print("hello world")

def function2():
    """FUNCTION DOCSTRING"""
    print("hello world")

def function3():
    """FUNCTION DOCSTRING"""
    print("hello world")

def main():
    """main function"""
    function()
    function2()
    function3()
    lass = NewClass()
    lass.func2()
    sm_class = SomeClass(1, '2', '3', '4', Value1="Shark", Value2=4.5, Value3=True)
    sm_class.printSomething()

if __name__ == "__main__":
    main()
