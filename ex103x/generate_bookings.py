#!/usr/bin/env python2

import sys
import random

#Local files
import data

requests_file_name = "requests"
filename = "bookings"

def request_confirmed():
    # Set probability for request to get accepted.
    return random.randint(0,100) < 80

def get_room_from_type(room_type):
    room_numbers = data.rooms.keys()
    return random.choice(room_numbers)

def main(args):
    with open(requests_file_name, "r") as requests:
        with open(filename, "w") as f:
            booking_id = 0
            for request_line in requests:
                if request_confirmed():
                    request_line_parts = request_line.split("|")
                    booking_id += 1
                    room = get_room_from_type(request_line_parts[2])
                    start_date = request_line_parts[4]
                    end_date = request_line_parts[5]
                    request_id = request_line_parts[0]
                    f.write("{}|{}|{}|{}|{}\n".format(booking_id, room,
                        start_date, end_date, request_id))                    

if __name__ == "__main__":
    random.seed()
    main(sys.argv[1:])
