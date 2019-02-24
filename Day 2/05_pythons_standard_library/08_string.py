import string

# Very useful constants:

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.digits)

print(string.hexdigits)

print(string.octdigits)

print(string.punctuation)

print(string.printable)

print(string.whitespace)


# Templates and formatting:
s = string.Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))
