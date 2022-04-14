from os import name

import barrage_of_questions
import directions
import results
import room
import random
import verification




def sanity_check(sanity):
    if sanity >= 13:
        return f'{sanity}\nYou are feeling focused and clear headed'
    elif 7 <= sanity <= 12:
        print(f'{sanity}\nBreath in through your nose, out through your mouth')
    elif 0 < sanity <= 6:
        print(f'{sanity}\nHanging on by a thread is putting it nicely..\n' +
            'Not gonna lie, things have definitely been better')
    else:
        print('You okay buddy? No, you are most definitely not.')


def player_status(self, location, inventory, sanity):
    sanity_check()
    item_list = room.rooms[location].get('item')
    if item_list == "":
        item_list = "Wow, nothing"
    else:
        item_list = item_list
    # print players current statistics
    print(f"\n**===**===****===**Current Status**===****===**===**\n" +
        f"Location: {location}\n" +
        f"Sanity: {sanity}\n" +
        f"What's In Your Inventory?: {inventory}\n"
        f"Whats in the room?: {item_list}\n" +
        '**===**===**===**===**===**===**===**===**===**===**')


def check_child():
    poss_room = random.choice('rooms')
    return poss_room


def ask_question(self):
    if check_child() == self.location:
        if self.location == 'Bathroom':
            print("""'I made Moana swim in the toilet, but shes stuck! Why is there so much water?'\n" + 
            "The toilet is thoroughly backed up and water is flooding across the bathroom floor, lose 5 sanity" 
            """)
        elif self.location == 'Living Room':
            print("'I got out ALL THE LEGOS!\nDON'T STEP ON MY TOWN!'\n"
                  'You step on multiple lego blocks, eviscerating the sole of your foot, lose 5 sanity\n')
        self.sanity -= 5
        rand_q = barrage_of_questions.question
        rand_a = barrage_of_questions.answer
        query = input(f"{self.pname},{self.pname},{self.pname}!\n{rand_q}\nTell me! {self.pname}!\n" +
                      "Your child is awaiting a response\nPlease press: 1 OR 2\n> ")
        print(f'You respond: {rand_a}\n')
        if query == 1:
            print(f"\nGood job {self.pname}!\n"
                  f"The child returns to the household wilderness\n")
        else:
            self.sanity += 3
            print(f"{self.pname.upper()} NO! NO! NO! NO! NO! NO! WRONG! WRONG! WRONG!")


def main():

    class Player:
        def __init__(self, name, pname, sanity, location, inventory):
            self.self = self,
            self.name = name,
            self.pname = pname,
            self.sanity = sanity,
            self.location = location,
            self.inventory = inventory,

    inventory = []
    location = 'Foyer'
    sanity = 20
    print(directions.show_instructions)
    name = input("'What's your preferred name?':\n>")
    pname = input("What name does the kiddo call you by?\n>")
    print("**===**===**===**===**===**===**===**===**===**===**\n" +
          f'Welcome to your parenting experience {name}\n\n')

    while True:
        player_status()
        move = ''
        print(move)
        while move == '':
            move = input('>')

        move = move.lower().split(" ", 1)

        if move[0] == 'go':
            if move[1] in room.rooms[location]:
                location = room.rooms[location][move[1]]
                check_child()
                ask_question(pname)
            else:
                verification.inaccessible()

        if move[0] == 'get':
            if "item" in room.rooms[location] and move[1] in room.rooms[location]['item']:
                # add the item to their inventory
                inventory += [move[1]]
                # display a helpful message
                print(f'You placed {[move[1]]}, in your inventory')
                # delete the item from the room
                del room.rooms[location]['item']
                # otherwise, if the item isn't there to get
            else:
                verification.not_there()

        # else:
        #     print('no')
        #     print(f'{name}, {move[1]} HAS NOT been added to your inventory')
        # check = f'You picked up, {verify}, do you want to add this to your inventory?\nY or N\n>'.upper()
        # if check == 'Y':
        #     inventory += [move[1]]
        #         print(f'You placed {[move[1]]}, in your inventory')
        #         del rooms[location]['items']
        #     else:
        #         print(f'{name}, {verify} HAS NOT been added to your inventory')
        #
        # elif rooms[location]['items'].len() == 0:
        #     verification.not_there()
        #
        # elif rooms[location]['items'].len() >= 2 and rooms[location]['items'].len() <= 3:
        #     item_check = input(f'{name}, please select an item from the list:\n {rooms[location]["items"]}').lower()
        #     if item_check in rooms[location]['items']:
        #         verify = item_check
        #         check = (f'You picked up, {verify}, do you want to add this to your inventory?\n Y or N\n>> ').upper()
        #         if check == 'Y':
        #             inventory += verify
        #             print(f'You placed {verify}, in your inventory')
        #             del rooms[location]['items'][verify]
        #         else:
        #             print(f'{name}, {verify} HAS NOT been added to your inventory')

        if location == 'Car'.lower() and 'Car Keys'.lower() in inventory and 'House Keys'.lower() in inventory and 'Wallet'.lower() in inventory \
                and sanity > 0:
            results.winner()
            break
        elif sanity < 0 and 'Car Keys' not in inventory and 'House Keys' not in inventory and 'Wallet' not in inventory:
            print(f'{name}, you were not strong enough, you lost your mind, and your keys, you cannot escape.')
            break


if __name__ == "__main__":
    main()
