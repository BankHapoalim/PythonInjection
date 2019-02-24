# Namespaces & objects in python can indicate that a certain property is private/internal by starting with "__"
# For example, each module has a __file__ attribute that contains a string with the module's filename:

print("Current module file path:", __file__)

print("Current module scope:", __name__)

if __name__ == "__main__":
    print("This line will be printed only if we're running on the main scope.")