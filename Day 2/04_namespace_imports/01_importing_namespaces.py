# Import the os module namespace into our own module namespace, under the "os" name:
import os

# Using attribute of another module:
print("Operating system type:", os.name)

# Using a function of another module:
print("Current working directory:", os.getcwd())

# The os module has a submodule named "path" for path operations, we can also access "path":
print("Windows directory exists?:", os.path.exists("C:\\Windows"))

