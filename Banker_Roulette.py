# Banker Roulette – Pick a random person to pay the bill

import random

friends = ["Alice", "Jack", "Bob", "Julia", "Ed", "Sonal"]

rand_friend = random.choice(friends)
print(rand_friend)

# OR

random_num = random.randint(0, 5)
print(friends[random_num])