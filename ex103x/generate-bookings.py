#!/usr/bin/env python2

import sys
import random
from datetime import datetime
from datetime import timedelta

rooms = {
    "normal_room": range(1, 100),
    "double_room": range(101, 200),
    "deluxe_room": range(201, 300),
    "conference_room": range(301, 310)
}

def request_confirmed():
    # Set probability for request to get accepted.
    return random.randint(0,100) < 80

def get_room_from_type(room_type):
    room_numbers = rooms[room_type]
    return random.choice(room_numbers)

def main(args):
    requests_file_name = args[0]
    output_file_name = args[1]
    with open(requests_file_name, "r") as requests:
        with open(output_file_name, "w") as f:
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
