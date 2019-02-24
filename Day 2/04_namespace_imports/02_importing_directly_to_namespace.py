# To import any attribute/function/submodule into our namespace directly, we can use the following:
from os import getlogin

# Since getlogin is imported directly into my namespace, I can now use it like this:
print("Username:", getlogin())

# One more example:
from os.path import isfile
print("Is the Windows directory a file?", isfile("C:\\Windows"))


# Importing everything from another module into my own namespace: (Bad practice!)
from os.path import *
print("Is the Windows directory a directory?", isdir("C:\\Windows"))
