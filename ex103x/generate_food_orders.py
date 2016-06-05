#!/usr/bin/env python2

import sys
import random
from datetime import datetime
from datetime import timedelta
from datetime import time

import data

filename = "food-orders"

num_orders = 6000

def random_room():
    room_type = random.choice(data.rooms.keys())
    return random.choice(data.rooms[room_type]["numbers"])

def main(args):
    with open(filename, "w+") as f:
        for i in range(0, num_orders):
            food_dest = random_room()
            bill_dest = random_room()
            date = datetime.now().date() - timedelta(random.randint(1, 100))
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            time_ = time(hour, minute)
            num_servings = random.randint(1, 5)
            menu_id = random.choice(data.menu.keys())
            f.write("{}|{}|{}|{}|{}|{}\n".format(food_dest, bill_dest, date, time_, num_servings, menu_id))

if __name__ == "__main__":
    random.seed()
    main(sys.argv[1:])
