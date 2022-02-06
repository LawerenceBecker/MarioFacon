### Events
## Start
# Event that play once when entering the room for the fist time
# [['MethodName', [kargs]], BennTriggered]

## S
# 1st step on event
## z
# 2nd step on event
## T
# 1st trigger event
## h
# 2nd trigger event

from eventTile import EventTile

maps = {

    'escape_pen': {
        "Transitions": [None, 'combat_tut', None, None],
        "MapLayout": [
            ['f','f','f','f','f','f','f','f',' ',' '],
            ['f',' ',' ','b',' ',' ','0','f',' ',' '],
            ['f','1',' ','f',' ',' ',' ','f',' ',' '],
            ['f','f','f','f',' ',' ',' ','f','f','f'],
            ['f',' ',' ',' ',' ',' ',' ','b',' ','e'],
            ['f',' ','p',' ',' ',' ',' ','f','f','f'],
            ['f',' ',' ',' ',' ',' ',' ','f',' ',' '],
            ['f',' ',' ',' ',' ',' ',' ','f',' ',' '],
            ['f','f','f','f','f','f','f','f',' ',' '],
        ],
        "Items": {
            '0': ['Carrot', False],
            '1': ['Strawberry', False],
        },
        "Events": {
            "Start": [['ScreenText', 'Escape the pen'], False],
        },
    },

    'combat_tut': {
        "Transitions": [None, None, None, 'escape_pen'],
        "MapLayout": [
            [' ',' ',' ',' ','f','f','f','f','f','f',],
            [' ',' ',' ',' ','f',' ',' ',' ','0','f',],
            ['f','f','f','f','f',' ',' ',' ',' ','f',],
            ['w',' ',' ',' ',' ','S',' ',' ',' ','f',],
            ['f','f','f','f','f',' ',' ',' ',' ','f',],
            [' ',' ',' ',' ','f',' ',' ',' ',' ','f',],
            [' ',' ',' ',' ','f','f','f','f',' ','f',],
            [' ',' ',' ',' ',' ',' ',' ','f',' ','f',],
            [' ',' ',' ',' ',' ',' ',' ','f','s','f',],
        ],
        "Items": {
            '0': ['Carrot', False],
        },
        "Events": {
            'S': [[EventTile.combat_Tut, None], False]
        }
    },

}