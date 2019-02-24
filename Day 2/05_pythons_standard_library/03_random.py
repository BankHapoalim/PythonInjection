import random

print(random.random())  # Random float between 0 and 1
print(random.randint(0,10))  # Random int betwwen 0 and 10

beatles = ["John", "Paul", "George", "Ringo"]

print(random.choice(beatles))  # Return a random choice from a sequence

random.shuffle(beatles)  # Shuffle the list `beatles`
print(beatles)
