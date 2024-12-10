import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.randint(0,4)
print(friends[random_friend])

print(random.choice(friends))