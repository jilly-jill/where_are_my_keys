import ascii
import childs_play
import directions
import player
import results
import room
import verification

#TODO Create Timer class and set timing for instances
def main():
    directions.start()
    name = player.player_name()
    pname = player.player_nickname()
    sanity = player.player_sanity()
    inventory = []
    usr = player.Player(name, pname, sanity, inventory)
    current_room = "Foyer"
    #TODO Clean up ASCII art
    print(ascii.head_01(),
        "\n**===**===**===**===**===**===**===**===**===**===**\n" +
        f'\nWelcome to your parenting experience {usr.name}\n')

    while True:
        player.player_status(usr.name, usr.inventory, usr.sanity, current_room)
        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split(" ", 1)
        if move[0] == 'go':
            if move[1] in room.rooms[current_room]:
                current_room = room.rooms[current_room][move[1]]
                check = childs_play.check_child()
                if check is True:
                    usr.sanity = childs_play.penalty(current_room, usr.sanity)
                    usr.sanity = childs_play.q_and_a(current_room, usr.sanity, usr.pname)
            else:
                verification.inaccessible(usr.name)

        if move[0] == 'get':
            if "item" in room.rooms[current_room] and move[1] in room.rooms[current_room]['item']:
                # add the item to their inventory
                usr.inventory += [move[1]]
                print(f'You added the following to your inventory:\n'
                      f'{move[1].upper()}\n')
                del room.rooms[current_room]["item"]
            else:
                verification.not_there(usr.name)

        if current_room.lower() == 'car' and 'car keys' in usr.inventory and 'house keys' in usr.inventory and \
                'wallet' in usr.inventory and usr.sanity > 0:
            results.winner()
            break
        elif usr.sanity <= 0:
            print(f'{usr.name}, you were not strong enough, you lost your mind, and your keys, you cannot escape.')
            break


if __name__ == "__main__":
    main()
