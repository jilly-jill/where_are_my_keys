import randomize
import room



def sanity_check(sanity, name):
    if sanity >= 13:
        return f'{sanity}\n{name}, you are feeling focused and clear headed\n'
    elif 7 <= sanity <= 12:
        return f'{sanity}\n{name}, I need you to breath in through your nose,\n ' \
               f'& out through your mouth\n'
    elif 0 < sanity <= 6:
        return f'{sanity}\nHanging on by a thread is putting it nicely' \
               f'{name}..\nNot gonna lie, things have definitely '\
               f'been better.'
    else:
        print(f'You okay buddy? No {name}, you are most definitely not.')

# TODO: Format inventory for player_status
def player_status(name, inventory, sanity, location):
    sanity = sanity_check(sanity, name)
    item_list = room.rooms[location].get('item')
    if item_list == "":
        item_list = "A rare clutterless room"
    else:
        item_list = item_list
    # print players current statistics

    print(
        f"**===**======**Hello God, it's me {name}**======**===**\n"
        f"Current Sanity: {sanity}\n"
        f"\nWhat's In Your Inventory?:{inventory}\n"
        f"Location: {location}\n"
        f"Whats in the room?: {item_list}\n"   
        f'**===================================================**\n'
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

class Player:
    def __init__(self, name, pname, sanity, inventory):
        self.name = name
        self.pname = pname
        self.sanity = sanity
        self.inventory = inventory
