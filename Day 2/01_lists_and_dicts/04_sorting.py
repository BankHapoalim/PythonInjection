mixed_list = [5, 19, 8, 11, 14, 1, 34, 6]

# sorted() returns a new sorted list from any sequence
print(sorted(mixed_list))

# list.sort() will sort the actual list object.
mixed_list.sort()
print(mixed_list)


numbers_dict = {5: "Five", 3: "Three", 1: "One", 2: "Two", 4: "Four"}

# Print the dictionary values ordered by their respective key.
for key in sorted(numbers_dict.keys()):
    print(numbers_dict[key])
