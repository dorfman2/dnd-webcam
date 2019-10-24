import json, time


if __name__ == '__main__':
    while True:
        move = input("direction? ")

        with open('move.json', 'w') as json_file:
            json.dump(move, json_file)
            time.sleep(3)
            move = False
            json.dump(move, json_file)
