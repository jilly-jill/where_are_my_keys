import randomize
import room


def sanity_check(sanity):
    if sanity >= 13:
        return f'{sanity}\nYou are feeling focused and clear headed'
    elif 7 <= sanity <= 12:
        return f'{sanity}\nBreath in through your nose, out through your mouth'
    elif 0 < sanity <= 6:
        return f'{sanity}\nHanging on by a thread is putting it nicely..\nNot gonna lie, things have definitely '\
               f'been better '
    else:
        print('You okay buddy? No, you are most definitely not.')


def player_status(inventory, sanity, location):
    # sanity_check(sanity)
    item_list = room.rooms [location].get('item')
    if item_list == "":
        item_list = "A rare clutterless room"
    else:
        item_list = item_list
    # print players current statistics
    print(
        f"**===**===****===**Current Status**===****===**===**\n"\
        f"Location: {location}\n"\
        f"Sanity: {sanity}\n"\
        f"What's In Your Inventory?:{inventory}\n"\
        f"Whats in the room?: {item_list}\n"\
        '**===**===**===**===**===**===**===**===**===**===**\n'
    )


def player_nickname():
    pname = input("What name does the kiddo call you by?\n>").capitalize()
    return pname


def player_name():
    name = input("What name do you prefer?\n>").capitalize()
    return name


def player_sanity(sanity=20):
    sanity - randomize.randomize_small()
    return sanity


def player_inventory():
    inventory = []
    return inventory


class Player:
    def __init__(self, name, pname, sanity, inventory):
        self.name = name
        self.pname = pname
        self.sanity = sanity
        self.inventory = inventory
