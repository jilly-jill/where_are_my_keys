import barrage_of_questions
import directions
import results
import room
import verification


class Player:
    def __init__(self, name, pname, inventory, sanity):
        self.name = name,
        self.pname = pname,
        self.inventory = inventory,
        self.sanity = sanity


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
    item_list = room.rooms[location].get('item')
    if item_list == "":
        item_list = "A rare clutterless room"
    else:
        item_list = item_list
    # print players current statistics
    print(
        f"**===**===****===**Current Status**===****===**===**\n" +
        f"Location: {location}\n" +
        f"Sanity: {sanity}\n" +
        f"What's In Your Inventory?: {inventory}\n"
        f"Whats in the room?: {item_list}\n" +
        '**===**===**===**===**===**===**===**===**===**===**'
    )


def main():
    directions.start()
    name = input("'What's your preferred name?':\n>")
    pname = input("What name does the kiddo call you by?\n>")
    usr = Player(name, pname, [], 20)
    current_room = 'Foyer'
    print(
        "\n**===**===**===**===**===**===**===**===**===**===**\n" +
        f'\nWelcome to your parenting experience {usr.name}\n')
    counter = 0
    while True:
        player_status(usr.inventory, usr.sanity, current_room)
        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split(" ", 1)
        if move[0] == 'go':
            if move[1] in room.rooms[current_room]:
                current_room = room.rooms[current_room][move[1]]
                check = barrage_of_questions.check_child()
                if check is True:
                    usr.sanity = barrage_of_questions.penalty(current_room, usr.sanity)
                    usr.sanity = barrage_of_questions.q_and_a(current_room, usr.sanity, usr.pname)
            else:
                verification.inaccessible(usr.name)

        if move[0] == 'get':
            if "item" in room.rooms[current_room] and move[1] in room.rooms[current_room]['item']:
                # add the item to their inventory
                usr.inventory += move[1]
                # display a helpful message
                print(f'You placed {move[1]}, in your inventory')
                # delete the item from the room
                del room.rooms[current_room]['item']
                # otherwise, if the item isn't there to get
            else:
                verification.not_there(usr.name)

        counter += 1
        print(counter)
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

        if current_room == 'Car' and 'Car Keys' in usr.inventory and 'House Keys' in usr.inventory and 'Wallet' in \
                usr.inventory and usr.sanity > 0:
            results.winner()
            break
        elif usr.sanity <= 0 and 'Car Keys' not in usr.inventory and 'House Keys' not in usr.inventory and 'Wallet' \
                not in usr.inventory:
            print(f'{usr.name}, you were not strong enough, you lost your mind, and your keys, you cannot escape.')
            break


if __name__ == "__main__":
    main()
