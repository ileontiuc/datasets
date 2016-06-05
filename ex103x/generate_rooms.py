#!/usr/bin/env python2

import sys

import data

filename = "rooms"

def main(args):
    entry_id = 0
    with open(filename, "w+") as f:
        for room in data.rooms.keys():
            entry_id += 1
            price = data.rooms[room]["price"]
            capacity = data.rooms[room]["capacity"]
            f.write("{}|{}|{}|{}\n".format(entry_id, price, capacity, room))

if __name__ == "__main__":
    main(sys.argv[1:])

