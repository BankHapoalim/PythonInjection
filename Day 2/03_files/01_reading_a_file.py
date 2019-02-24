###################################
# Read entire file into a string: #
###################################

file_object = open("example.txt", "r")  # "r" is the default mode.

# An optional argument can be specified to read() to indicate amount of chars to read.
# No argument means read everything until the end of file.
file_content = file_object.read()

file_object.close()

print("The content of example.txt as one string:")
print(file_content)


print("="*20)
#################################
# Read all file lines into list #
#################################

file_object = open("example.txt", "r")  # "r" is the default mode.

list_of_lines = file_object.readlines()

file_object.close()


print("The content of example.txt as list of lines:")
print(list_of_lines)
