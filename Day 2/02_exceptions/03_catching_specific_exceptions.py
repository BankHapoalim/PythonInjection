# Catch a specific exception object

x = "10"
while x.isdigit():
    try:
        print("100 divided by %s is %s" % (x, 100 / int(x)))
    except ZeroDivisionError:
        print("Only Chuck Norris can divide by zero.")
    except ValueError:
        print("There was a problem with the value entered.")

    x = input("Enter a number that will divide 100: ")

print("The entered number was not a digit, exiting...")
