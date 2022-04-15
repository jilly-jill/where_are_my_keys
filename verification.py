import random


def inaccessible(name):
    possibilities = [f"\nIt's okay {name}, you're tired, but you can't walk through a wall",
                     f"\n{name}, did you consider that walls don't work like that?",
                     "Here Be Dragons...", f"Hey {name}, physics will stop you everytime.."]
    invalid = random.choice(possibilities)
    print(invalid)


def no_input_detected(name):
    possibilities = [f"\n{name},I know you can do it, lets try putting that in again!",
                     f"\n& I thought I was tired, {name} let's try that again.",
                     f"\n{name}, did you fat finger or are you not paying attention? I need some input here"]
    invalid = random.choice(possibilities)
    print(invalid)

def not_there(name):
    possibilities = [f"\n{name} why are we reaching for intangibles? There's nothing there!",
                     f"\nYou do realize to take something, it has to be there, right? {name}",
                     f"\n{name}, {name}, {name}, get it together, there's nothing there"]
    invalid = random.choice(possibilities)
    print(invalid)

# def check_input():
#     if input == '':
# 	    no_input_detected()
