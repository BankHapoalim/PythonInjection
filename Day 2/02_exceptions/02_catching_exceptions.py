# Catch all exceptions: (Bad practice!)

x = "10"
while x.isdigit():
    try:
        print("100 divided by %s is %s" % (x, 100 / int(x)))
    except:
        print("Oh no! something bad happened, lets try again.")

    x = input("Enter a number that will divide 100: ")

print("The entered number was not a digit, exiting...")
