''' DMX lighting setup

        [ Stage / Front ]

    [R]                 [R]
[R] [C] [R]         [R] [C] [R]

        [S]   (D)   [S]

R: RGB Can
C: White Spot
S: RGB Spot
D: Disco Ball

        [ Stage / Front ]
    [4]                 [2]
[5] [ ] [6]         [3] [ ] [1]

        [8]   ( )   [7]
'''


STAGE_RIGHT = {'front': 49,
               'right': 65,
               'left': 81
               }
STAGE_LEFT = {'front': 17,
              'right': 33,
              'left': 1
              }
DISCO = {'left': 97,
         'right': 113
         }

RGB_CAN_PROFILE = {"power": 0,
                   "red": 1,
                   "green": 2,
                   "blue": 3,
                   "white": 4,
                   "selection": 5,
                   "speed": 6,
                   "strobe": 7}

RGB_SPOT_PROFILE = {"power": 0,
                    "red": 1,
                    "green": 2,
                    "blue": 3,
                    "strobe": 4
                    }
