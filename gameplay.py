
import directions
import kiddo
import results
import room
import random
import verification

def sanity_check():
    if sanity >= 13:
        return(f'{sanity}\nYou are feeling focused and clear headed')
    elif 7 <= sanity <= 12:
        print(f'{sanity}\nBreath in through your nose, out through your mouth')
    elif 0 < sanity <= 6:
        print(f'{sanity}\nHanging on by a thread is putting it nicely..\n' +
        'Not gonna lie, things have definitely been better')
    else:
        print('You okay buddy? No, you are most definitely not.')

def playerStatus():
    sanity = sanity_check()
    item_list = room.rooms[location].get('item')
    if item_list == "":
        item_list = "Wow, nothing"
    else:
        item_list = item_list
    #print players current statistics
    print(f"\n**===**===****===**Current Status**===****===**===**\n" +
            f"Location: {location}\n" +
            f"Sanity: {sanity}\n" +
            f"What's In Your Inventory?: {inventory}\n"
            f"Whats in the room?: {item_list}\n" +
          '**===**===**===**===**===**===**===**===**===**===**')

inventory = []
sanity = 20
location = 'Foyer'
print(directions.show_instructions)
name = input("\n**===**===**===**===**===**===**===**===**===**===**\n" +
           "What's your preferred name?:\n>")
pname = input("\n**===**===**===**===**===**===**===**===**===**===**\n" +
              "What name does the kiddo call you by?\n>")
print("**===**===**===**===**===**===**===**===**===**===**\n" +
f'Welcome to your parenting experience {name}\n\n')

while True:
    playerStatus()

    move = ''
    print(move)
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        kiddo.appear
        if move[1] in room.rooms[location]:
            location = room.rooms[location][move[1]]
        else:
            verification.inaccessible()

    if move[0] == 'get':
        item_ch = room.rooms[location]
        check = room.rooms[location]['item'].capitalize()
        # if the room contains an item, and the item is the one they want to get
        if "item" in item_ch and move[1] in check:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(f'You placed {[move[1]]}, in your inventory')
            # delete the item from the room
            del room.rooms[location]['item']
        # otherwise, if the item isn't there to get
        else:
            verification.not_there()
        # if move[1] in room.rooms[location]['item']:
        #     inventory += [move[1]]
        #     print(f'You placed {[move[1]]}, in our inventory')
        #     del room.rooms[location]['item']
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
