from os import name

import barrage_of_questions
import directions
import results
import room
import random
import verification


def ask_question(location, sanity, pname):
    if check_child() == location:
        if location == 'Bathroom':
            print(
                """'I made Moana swim in the toilet, but shes stuck! Why is there so much water?'\n" + 
                        "The toilet is thoroughly backed up and water is flooding across the bathroom floor, lose 5 sanity" 
                        """
            )
        elif location == 'Living Room':
            print(
                "'I got out ALL THE LEGOS!\nDON'T STEP ON MY TOWN!'\n"
                'You step on multiple lego blocks, eviscerating the sole of your foot, lose 5 sanity\n'
            )
        sanity -= 5
        rand_q = barrage_of_questions.question
        rand_a = barrage_of_questions.answer
        query = input(
            f"{pname},{pname},{pname}!\n{rand_q}\nTell me! {pname}!\n" +
            "Your child is awaiting a response\nPlease press: 1 OR 2\n> "
        )
        print(f'You respond: {rand_a}\n')
        if query == 1:
            print(
                f"\nGood job {pname}!\n"
                f"The child returns to the household wilderness\n"
            )
        else:
            sanity += 3
            print(f"{pname.upper()} NO! NO! NO! NO! NO! NO! WRONG! WRONG! WRONG!")


def sanity_check(sanity):
    if sanity >= 13:
        return f'{sanity}\nYou are feeling focused and clear headed'
    elif 7 <= sanity <= 12:
        print(f'{sanity}\nBreath in through your nose, out through your mouth')
    elif 0 < sanity <= 6:
        print(
            f'{sanity}\nHanging on by a thread is putting it nicely..\n' +
            'Not gonna lie, things have definitely been better'
        )
    else:
        print('You okay buddy? No, you are most definitely not.')


def player_status(inventory, sanity, location):
    # sanity_check(sanity)
    item_list = room.rooms [location].get('item')
    if item_list == "":
        item_list = "Wow, nothing"
    else:
        item_list = item_list
    # print players current statistics
    print(
        f"\n**===**===****===**Current Status**===****===**===**\n" +
        f"Location: {location}\n" +
        f"Sanity: {sanity}\n" +
        f"What's In Your Inventory?: {inventory}\n"
        f"Whats in the room?: {item_list}\n" +
        '   **===**===**===**===**===**===**===**===**===**===**'
    )


class Player:
    def __init__(self, name, pname, inventory, sanity):
        self.name = name,
        self.pname = pname,
        self.inventory = inventory,
        self.sanity = sanity


def check_child(currentRoom):
    poss_room = random.choice('T' 'F')
    print(poss_room + currentRoom)
    if poss_room == currentRoom:
        return True
    else:
        return False

def main():
    print(directions.show_instructions)
    name = input("'What's your preferred name?':\n>")
    pname = input("What name does the kiddo call you by?\n>")
    usr = Player(name, pname, [], 20)
    print(type(usr.sanity))
    currentRoom = 'Foyer'
    print(directions.show_instructions)
    print(
        "**===**===**===**===**===**===**===**===**===**===**\n" +
        f'Welcome to your parenting experience {usr.name}\n\n'
    )

    while True:
        player_status(usr.inventory, usr.sanity, currentRoom)
        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split(" ", 1)
        if move[0] == 'go':
            if move[1] in room.rooms[currentRoom]:
                currentRoom = room.rooms[currentRoom][move[1]]
                if check_child(currentRoom) == True:
                    ask_question(currentRoom, usr.sanity, usr.pname)
            else:
                verification.inaccessible()

        if move[0] == 'get':
            if "item" in room.rooms[currentRoom] and move [1] in room.rooms[currentRoom]['item']:
                # add the item to their inventory
                usr.inventory += [move[1]]
                # display a helpful message
                print(f'You placed {[move [1]]}, in your inventory')
                # delete the item from the room
                del room.rooms [currentRoom]['item']
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

        if currentRoom == 'Car'.lower() and 'Car Keys'.lower() in usr.inventory and 'House Keys'.lower() in usr.inventory and 'Wallet'.lower() in usr.inventory\
                and usr.sanity > 0:
            results.winner()
            break
        elif usr.sanity < 0 and 'Car Keys' not in usr.inventory and 'House Keys' not in usr.inventory and 'Wallet' not in usr.inventory:
            print(f'{usr.name}, you were not strong enough, you lost your mind, and your keys, you cannot escape.')
            break


if __name__ == "__main__":
    main()
