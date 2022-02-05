### Events
## Start
# Event that play once when entering the room for the fist time
# [['MethodName', [kargs]], BennTriggered]

## E
# 1st step on event
## e
# 2nd step on event
## T
# 1st trigger event
## t
# 2nd trigger event

maps = {
    'TEST_MAP': [
        [None, 'test_map', None, None],
        [
            ['f','f','f','f','f','f','f',' ',' '],
            ['f',' ','1',' ',' ','2','f','f','f'],
            ['f',' ',' ','p',' ',' ','b',' ','e'],
            ['f','3',' ',' ',' ','4','f','f','f'],
            ['f','f','f','f','f','f','f',' ',' '],
        ],
        {
            "1": ["Strawberry", False], 
            "2": ["Carrot", False],
            "3": ["Strawberry", False], 
            "4": ["Carrot", False]
        },
    ],

    'test_map': [
        [None, None, None, 'TEST_MAP'],
        [
            [' ','f','f','f','f'],
            ['f','f',' ',' ','f'],
            ['w',' ','p',' ','f'],
            ['f','f',' ',' ','f'],
            [' ','f','f','f','f'],
        ],
        {}
    ],

    'escape_pen': [
        [None, 'combat_tut', None, None],
        [
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
        {
            '0': ['Carrot', False],
            '1': ['Strawberry', False],
        },
        {
            "Start": [['ScreenText', 'Escape the pen'], False],
        },
    ],

    'combat_tut': [
        [None, None, None, 'escape_pen'],
        [
            [' ',' ',' ',' ','f','f','f','f','f','f',],
            [' ',' ',' ',' ','f',' ',' ',' ','0','f',],
            ['f','f','f','f','f',' ',' ',' ',' ','f',],
            ['w',' ',' ',' ',' ',' ',' ',' ',' ','f',],
            ['f','f','f','f','f',' ',' ',' ',' ','f',],
            [' ',' ',' ',' ','f',' ',' ',' ',' ','f',],
            [' ',' ',' ',' ','f','f','f','f',' ','f',],
            [' ',' ',' ',' ',' ',' ',' ','f',' ','f',],
            [' ',' ',' ',' ',' ',' ',' ','f','s','f',],
        ],
        {
            '0': ['Carrot', False],
        }
    ]
}