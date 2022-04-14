import random
import gameplay
no_input_detected = " "
not_there = " "


def inaccessible():
    possibilities = [f"\nIt's okay {gameplay.name}, you're tired, but you can't walk through a wall",
                     f"\n{gameplay.name}, did you consider that walls don't work like that?",
                     "Here Be Dragons...", f"Hey {gameplay.name}, physics will stop you everytime.."]
    invalid = random.choice('possibilities')
    return invalid


def no_input_detected():
    possibilities = [f"\n{gameplay.name},I know you can do it, lets try putting that in again!",
                     f"\n& I thought I was tired, {gameplay.name} let's try that again.",
                     f"\n{gameplay.name}, did you fat finger or are you not paying attention? I need some input here"]
    invalid = random.choice('possibilities')
    input_detected_f = invalid
    return f'\n{input_detected_f}'


def not_there():
    possibilities = [f"\n{gameplay.name} why are we reaching for intangibles? There's nothing there!",
                     f"\nYou do realize to take something, it has to be there, right? {gameplay.name}",
                     f"\n{gameplay.name}, {gameplay.name}, {gameplay.name}, get it together, there's nothing there"]
    invalid = random.choice('possibilities')
    not_there = invalid
    return f'\n{not_there}'

# def check_input():
#     if input == '':
# 	    no_input_detected()
