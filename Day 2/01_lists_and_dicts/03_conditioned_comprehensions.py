some_int_list = [1, 2, 3, 4, 5, 6]

# Return a list containing only the doubled even numbers of another list

# Method 1: for loop + if-else
doubled_evens = []
for x in some_int_list:
    if x % 2 == 0:
        doubled_evens.append(x * 2)
print(doubled_evens)

# Method 2: list comprehension
doubled_evens = [x * 2 for x in some_int_list if x % 2 == 0]
print(doubled_evens)


# Conditions on a dict comprehension -
# Creating a new dictionary with only pairs where the value is larger than 2:
d = {'a': 1, 'b': 2, 'c': 3}
d = {k: v for (k, v) in d.items() if v > 2}
print(d)
