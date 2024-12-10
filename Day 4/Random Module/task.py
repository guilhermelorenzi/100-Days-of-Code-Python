import random
# import my_module
#
# random_integer = random.randint(1,10)
# print(random_integer)
#
# print(my_module.my_favourite_number)
#
# random_number_0_to_1 = random.random() *10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1,10)
# print(random_float)


random_heads_or_tails = random.randint(0,1)
print(random_heads_or_tails)

if random_heads_or_tails == 0:
    print("Heads")
elif random_heads_or_tails == 1:
    print("Tails")