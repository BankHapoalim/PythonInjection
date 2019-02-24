# Writing to a file

# Open the file in mode "w",
file_object = open("example-written.txt", "w")  # "r" is the default mode.

user_input = " "
while user_input:
    user_input = input("Enter line to write to a file:")
    file_object.write(user_input + '\n')

file_object.close()
