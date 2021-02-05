import random


def chance(percent):
    x = random.randint(0, 100)
    if x <= percent:
        return True
    else:
        return False


i_h = 0
n_h = 0
for i in range(10):

    if chance(50):

        i_h += 1

    else:

        n_h += 1
print(i_h, n_h)
