import randomize

rooms = {
    'Foyer': {
        'east': 'Dining Room',
        'north': 'Hall',
        'south': 'Outside',
        'item': 'clod of dirt',
        'id': '1'
    },
    'Dining Room': {
        'north': 'Kitchen',
        'west': 'Foyer',
        'item': 'wallet',
        'id': '2'
    },
    'Kitchen': {
        'south': 'Dining Room',
        'west': 'Hall',
        'item': 'cold coffee',
        'id': '3'
    },
    'Outside': {
        'north': 'Foyer',
        'east': 'Car',
        'item': 't-rex sock',
        'id': '4'
    },
    'Car': {
        'west': 'Outside',
        'item': 'blippi sock',
        'id': '5'
    },
    'Hall': {
        'north': 'Living Room',
        'west': 'Bedroom',
        'east': 'Kitchen',
        'south': 'Foyer',
        'item': 'capri sun straw wrappers',
        'id': '6'
    },
    'Bedroom': {
        'north': "Kid's Bedroom",
        'east': "Hall",
        'item': 'car keys',
        'id': '7'
    },
    "Kid's Bedroom": {
        'north': 'Bathroom',
        'south': 'Bedroom',
        'item': 'toy chest',
        'id': '8'
    },
    "Bathroom": {
        'south': "Kid's Bedroom",
        'east': 'Living Room',
        'item': 'blippi sock',
        'id' : '9'
    },
    "Living Room": {
        "west": 'Bathroom',
        'south': 'Hall',
        'item': 'house keys',
        'id': '10'
    }
}

