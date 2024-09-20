import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.choice(friends)

print(random_friend)

random_index = random.randint(0, len(friends) - 1)
print(friends[random_index])

