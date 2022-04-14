
import barrage_of_questions
import gameplay

sane = 0
child_in_room = " "
neg_bonus = -5

def ask_question():
    rand_q = barrage_of_questions.question
    rand_a = barrage_of_questions.answer
    query = input(f"{gameplay.pname},{gameplay.pname},{gameplay.pname}!\n{rand_q}\nTell me! {gameplay.pname}!\n" +
                    "Your child is awaiting a response\nPlease press: 1 OR 2")
    print(f'You respond: {rand_a}\n')
    if query == 1:
        print(f"\nGood job {gameplay.pname}!\n"
                f"The child returns to the household wilderness")
    else:
        penalty = 3
        print(f"{gameplay.pname.upper()} NO! NO! NO! NO! NO! NO! WRONG! WRONG! WRONG!")
        return penalty

question = ask_question()



