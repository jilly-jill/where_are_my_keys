

rooms = {
    'Foyer': {
        'east': 'Dining Room',
        'north': 'Hall',
        'south': 'Outside',
        'item': 'blippi sock',
    },
    'Dining Room': {
        'north': 'Kitchen',
        'west': 'Foyer',
        'item': 'wallet',
    },
    'Kitchen': {
        'south': 'Dining Room',
        'west': 'Hall',
        'item': 'travel mug of cold coffee',
    },
    'Outside': {
        'north': 'Foyer',
        'east': 'Car',
        'item': 'trex sock',
    },
    'Car': {
        'west': 'Outside',
        'item': 'blippi sock',
    },
    'Hall': {
        'north': 'Living Room',
        'west': 'Bedroom',
        'east': 'Kitchen',
        'south': 'Foyer',
        'item': '3 capri straw wrappers',
    },
    'Bedroom': {
        'north': "Kid's Bedroom",
        'east': "Hall",
        'items': 'dusty sleep mask',
    },
    "Kid's Bedroom": {
        'north': 'Bathroom',
        'south': 'Bedroom',
        'item': {
            'toy chest': 'car keys'
        }
    },
    "Bathroom": {
        'south': "Kid's Bedroom",
        'east': 'Living Room',
        'item': 'blippi sock'},

    "Living Room": {
        "west": 'Bathroom',
        'south': 'Hall',
        'item': 'a minefield of legos'
    }
}
