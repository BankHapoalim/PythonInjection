# Can a user cause an exception here?

x = "10"
while x.isdigit():
    print("100 divided by %s is %s" % (x, 100 / int(x)))
    x = input("Enter a number that will divide 100: ")

print("The entered number was not a digit, exiting...")

# What happens to our program when an exception is raised?

