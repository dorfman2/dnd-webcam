"""
This file is to test recieving JSON from Flask.app

"""

import time, json

move_up = True      # Motor1 Forward
move_down = True    # Motor1 Backward
move_left = True    # Motor2 Forward
move_right = True   # Motor2 Backward

def json_read():
    try:
        with open('move.json') as m:
            data = json.load(m)

    except FileNotFoundError:
            data = "File Not Found"

    print(data)

# Script

if __name__ == '__main__':


    while True:

        direction = json_read()


        if direction == False:
            print('Up')
        elif move_down == False:
            print('Down')
        else:
            print('#')

        if move_left == False:
            print('Left')
        elif move_right == False:
            print('Right')
        else:
            print('.')

        time.sleep(0.25)