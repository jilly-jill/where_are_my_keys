import random


questions = ["Do fish fart?", "What does blue taste like?", "What time is it yesterday?", "Do dogs dream"]
answers = ["Yes", "No", "Sure", "Orange", "62:00PM"]


def check_child(location, sanity, pname):
    c = random.randrange(1, 10)
    if c < 5:
        q_and_a(location, sanity, pname)
        if location == 'Bathroom' or location == 'Living Room':
            if location == 'Bathroom':
                print(
                    "'I made Moana swim in the toilet, but shes stuck! Why is there so much water?'\n" +
                    "The toilet is thoroughly backed up and water is flooding across the bathroom floor!'\nLOSE 5 "
                    "SANITY POINTS! "
                )
            elif location == 'Living Room':
                print(
                    "'I got out ALL THE LEGOS!\nDON'T STEP ON MY TOWN!'\n" +
                    'You step on multiple lego blocks, eviscerating the sole of your foot, lose 5 sanity\n'
                )
            sanity -= 5
            return sanity


def q_and_a(location, sanity, pname):
    print(location)
    question = random.choice(questions)
    number = random.randrange(1, 10)

    input("QUICK! You've been spotted by a feral toddler! Press any key to continue\n>")
    answer = input(
        f"Tell me! {question}, {pname}!\nYour child is awaiting a response\n" +
        "What is your response?:\n> "
        ).capitalize()
    print(f'You respond: {answer}\n')
    if number > 5:
        sanity -= 3
        print(f"{pname} NO! NO! NO! NO! NO! NO! THAT'S WRONG! WRONG! WRONG!")
    else:
        print(
            f"\nGood job {pname}!\n"
            "The child returns to the household wilderness"
            )
    return sanity
