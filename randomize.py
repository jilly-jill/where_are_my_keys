import random


def randomize_item(need_randomized):
    rand = random.choice(need_randomized)
    return rand


def randomize_int():
    rand = random.randrange(1, 10)
    return rand


def randomize_small():
    rand = random.randrange(0, 3)
    return rand
