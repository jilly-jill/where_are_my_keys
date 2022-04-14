
import random


rooms = {
    'Foyer': {
        'east': 'Dining Room',
        'north': 'Hall',
        'south': 'Outside',
        'item': '1 Blippi Sock',
        'random': 'T'
    },
    'Dining Room': {
        'north': 'Kitchen',
        'west': 'Foyer',
        'item': 'Wallet',
        'random': 'T'

    },
    'Kitchen': {
        'south': 'Dining Room',
        'west': 'Hall',
        'item': 'Travel Mug of Cold Coffee',
        'random': 'F'
    },
    'Outside': {
        'north': 'Foyer',
        'east': 'Car',
        'item': '1 TRex Sock',
        'random': 'F'
    },
    'Car': {
        'west': 'Outside',
        'item': '1 Blippi Sock',

    },
    'Hall': {
        'north': 'Living Room',
        'west': 'Bedroom',
        'east': 'Kitchen',
        'south': 'Foyer',
        'item': '3 Capri Sun Straw Wrappers',
        'random': 'T'
    },
    'Bedroom': {
        'north': "Kid's Bedroom",
        'east': "Hall",
        'items': 'Dusty Sleep Mask',
        'random': 'T'
    },
    "Kid's Bedroom": {
        'north': 'Bathroom',
        'south': 'Bedroom',
        'east': 'Toy Chest',
        'item': 'Petrified PopTart',
        'random': 'F'
    },
    "Toy Chest": {
        'west': "Kid's Bedroom",
        'item': 'Car Keys'
    },
    "Bathroom": {
        'south': "Kid's Bedroom",
        'east': 'Living Room',
        'item': '1 Blippi Sock'},
        'random': 'F',

    "Living Room": {
        "west": 'Bathroom',
        'south': 'Hall',
        'item': 'House',
        'random': 'F'
    }
}



# if rooms.__contains__('Bathroom') or rooms.__contains__('Living Room'):
#     bathroom = rooms['Bathroom']
#     livingroom = rooms['Living Room']


