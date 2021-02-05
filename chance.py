import random
from collections import Counter

bag = {"potion": 2, "escape-rope": 1, "power-up": 0}
loot_pool = ["potion", "escape-rope", "power-up"]


# function to determine spawn
def chance(percent):
    x = random.randint(0, 100)
    if x <= percent:
        return True
    else:
        return False


# pick some loot
def loot():

    loot_dropped = random.choices(loot_pool, weights=[10, 7, 5], k=2)

    for loot in loot_dropped:

        if loot == "potion":
            bag["potion"] += 1

        elif loot == "escape-rope":
            bag["escape-rope"] += 1

        elif loot == "power-up":
            bag["power-up"] += 1
        else:
            break

        # count the number of items dropped
    c = Counter(loot_dropped)

    for keys, values in c.items():
        print("You found a", keys.capitalize(), "x", values, "!")


if chance(50):
    loot()
else:
    print("Unlucky")
