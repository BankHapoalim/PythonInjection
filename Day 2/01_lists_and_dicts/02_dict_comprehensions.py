test_names = ('Running', 'Jumping', 'Push-ups', 'Swimming')
test_scores = (10.52, 3.4, 35, 14.3)

# Method 1, simple loop:
test_dict = {}
for test_number in range(len(test_names)):
    test_dict[test_names[test_number]] = test_scores[test_number]
print(test_dict)


# Method 2, loop + zip:
test_dict = {}
for test_name, test_score in zip(test_names, test_scores):
    test_dict[test_name] = test_score
print(test_dict)


# Method 3, dict comprehension:
test_dict = {test_name: test_score for test_name, test_score in zip(test_names, test_scores)}
print(test_dict)