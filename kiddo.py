import random


import barrage_of_questions
import gameplay

sane = 0
child_in_room = " "
neg_bonus = -5

def ask_question():
    sane = gameplay.sanity
    rand_q = barrage_of_questions.question
    rand_a = barrage_of_questions.answer
    query = input(f"{gameplay.pname},{gameplay.pname},{gameplay.pname}!\n{rand_q}\nTell me! {gameplay.pname}!\n" +
                    "Your child is awaiting a response\nPlease press: 1 OR 2")
    print(f'You respond: {rand_a}\n')
    if query == 1:
        print(f"\nGood job {gameplay.pname}!\n"
                f"The child returns to the household wilderness")
    else:
        sane -= 3
        print(f"{gameplay.pname.upper()} NO! NO! NO! NO! NO! NO! WRONG! WRONG! WRONG!")
        return sane
    return sane

def child_appear():
    option = ['True', 'False']
    child_in_room = random.choice(option)
    return child_in_room

appear = child_appear()

if child_in_room == 'True':
    if gameplay.location == 'Bathroom':
        print(f'"{gameplay.pname}, I made Moana swim in the toilet, but shes stuck! Why is there so much water?"\n' +
              'The toilet is thoroughly backed up and water is flooding across the bathroom floor, lose 5 sanity\n')
    if gameplay.location == 'Living Room':
        print(f"'{gameplay.pname}, I got out ALL THE LEGOS!\n{gameplay.pname} DON'T STEP ON MY TOWN!'\n" +
                     'You step on multiple lego blocks, eviscerating the sole of your foot, lose 5 sanity\n')
    sanity = ask_question() + neg_bonus


