import random

numbers = [1, 3, 5, 7]
print(random.choice(numbers))

random.shuffle(numbers)
print(numbers)

print(random.randrange(1,7))