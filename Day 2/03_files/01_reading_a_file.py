
file_object = open("example.txt", "r")  # "r" is the default mode.

# An optional argument can be specified to read() to indicate amount of chars to read.
# No argument means read everything until the end of file.
file_content = file_object.read()

file_object.close()

print("The content of example.txt:")
print(file_content)
