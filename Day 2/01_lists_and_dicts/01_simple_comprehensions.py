some_int_list = [1, 2, 3, 4]

# The following two pieces of code do exactly the same:

# Method 1: Classic loop method:
doubled_int_list = []
for x in some_int_list:
    doubled_int_list.append(x * 2)
print(doubled_int_list)

# Method 2: List comprehension method
doubled_int_list = [x * 2 for x in some_int_list]
print(doubled_int_list)


# One more example with strings:
word_list = ['WordS', 'WITH', 'mixed', 'Casing']

# Method 1: Classic loop method:
lowercase_word_list = []
for word in word_list:
    lowercase_word_list.append(word.lower())
print(lowercase_word_list)

# Method 2: List comprehension method
lowercase_word_list = [word.lower() for word in word_list]
print(lowercase_word_list)
