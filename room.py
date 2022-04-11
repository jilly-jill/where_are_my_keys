
import random
import kiddo
import gameplay

rooms = {
    'Foyer': {
        'east': 'Dining Room',
        'north': 'Hall',
        'south': 'Outside',
        'item': '1 Blippi Sock'
    },
    'Dining Room': {
        'north': 'Kitchen',
        'west': 'Foyer',
        'item': 'Wallet'
    },
    'Kitchen': {
        'south': 'Dining Room',
        'west': 'Hall',
        'item': 'Travel Mug of Cold Coffee'
    },
    'Outside': {
        'north': 'Foyer',
        'east': 'Car',
        'item': '1 TRex Sock'
    },
    'Car': {
        'west': 'Outside',
        'item': '1 Blippi Sock'
    },
    'Hall': {
        'north': 'Living Room',
        'west': 'Bedroom',
        'east': 'Kitchen',
        'south': 'Foyer',
        'item': '3 Capri Sun Straw Wrappers'
    },
    'Bedroom': {
        'north': "Kid's Bedroom",
        'east': "Hall",
        'items': 'Dusty Sleep Mask'
    },
    "Kid's Bedroom": {
        'north': 'Bathroom',
        'south': 'Bedroom',
        'east': 'Toy Chest',
        'item': 'Petrified PopTart'
    },
    "Toy Chest": {
        'west': "Kid's Bedroom",
        'item': 'Car Keys'
    },
    "Bathroom": {
        'south': "Kid's Bedroom",
        'east': 'Living Room',
        'item': '1 Blippi Sock'
    },
    "Living Room": {
        'west': 'Bathroom',
        'south': 'Hall',
        'item': 'House Keys'
    }
}

def child_check():
    child_in_room = random.choice([True, False])
    if child_in_room == True:
        if gameplay.location == 'Bathroom':
            print(f'"{gameplay.pname}, I made Moana swim in the toilet, but shes stuck! Why is there so much water?"\n' +
                      'The toilet is thoroughly backed up and water is flooding across the bathroom floor, lose 5 sanity\n')
            sanity = gameplay.sanity
            sanity -= 5
            return sanity
        if gameplay.location == 'Living Room':
            print(f"'{gameplay.pname}, I got out ALL THE LEGOS!\n{gameplay.pname} DON'T STEP ON MY TOWN!'\n" +
                      'You step on multiple lego blocks, eviscerating the sole of your foot, lose 5 sanity\n')
            sanity = gameplay.sanity
            sanity -= 5
            return sanity
        else:
            #kiddo.scenario()
            kiddo.ask_question()

