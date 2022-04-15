
import random


rooms = {
    'Foyer': {
        'east': 'Dining Room',
        'north': 'Hall',
        'south': 'Outside',
        'item': '1 Blippi Sock',
    },
    'Dining Room': {
        'north': 'Kitchen',
        'west': 'Foyer',
        'item': 'Wallet',
    },
    'Kitchen': {
        'south': 'Dining Room',
        'west': 'Hall',
        'item': 'Travel Mug of Cold Coffee',
    },
    'Outside': {
        'north': 'Foyer',
        'east': 'Car',
        'item': '1 TRex Sock',
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
    },
    'Bedroom': {
        'north': "Kid's Bedroom",
        'east': "Hall",
        'items': 'Dusty Sleep Mask',
    },
    "Kid's Bedroom": {
        'north': 'Bathroom',
        'south': 'Bedroom',
        'east': 'Toy Chest',
        'item': 'Petrified PopTart',
    },
    "Toy Chest": {
        'west': "Kid's Bedroom",
        'item': 'Car Keys'
    },
    "Bathroom": {
        'south': "Kid's Bedroom",
        'east': 'Living Room',
        'item': '1 Blippi Sock'},

    "Living Room": {
        "west": 'Bathroom',
        'south': 'Hall',
        'item': 'House',
    }
}


