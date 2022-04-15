import random
import barrage_of_questions
import directions
import player
import results
import room
import verification


def main():
    directions.start()
    name = player.player_name()
    pname = player.player_nickname()
    sanity = player.player_sanity()
    inventory = player.player_inventory()
    usr = player.Player(name, pname, sanity, inventory)
    current_room = 'Foyer'
    print(
        "\n**===**===**===**===**===**===**===**===**===**===**\n" +
        f'\nWelcome to your parenting experience {usr.name}\n')

    counter = 0
    while True:
        player.player_status(usr.inventory, usr.sanity, current_room)
        move = ''
        while move == '':
            move = input('>').lower()
        move = move.lower().split(" ", 1)
        print(type(move), move)

        if move[0] == 'go':
            if move[1] in room.rooms[current_room]:
                current_room = room.rooms[current_room][move[1]]
                print(type(current_room), current_room)
                check = barrage_of_questions.check_child()
                if check is True:
                    usr.sanity = barrage_of_questions.penalty(current_room, usr.sanity)
                    print(type(usr.sanity), usr.sanity)
                    usr.sanity = barrage_of_questions.q_and_a(current_room, usr.sanity, usr.pname)
                    print(type(usr.sanity), usr.sanity)
            else:
                verification.inaccessible(usr.name)

        if move[0] == 'get':
            if "item" in room.rooms[current_room] and move[1] in room.rooms[current_room]['item']:
                # add the item to their inventory
                print(type(move[1]), move[1], usr.inventory)
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
