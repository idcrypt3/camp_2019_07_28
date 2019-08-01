import random
print("Your random dice roll is...")
print(random.randint(1, 12))


def random_number(max_int):
    rand = random.randrange(0, max_int)
    return rand

a_number = random_number(5)
print(a_number)