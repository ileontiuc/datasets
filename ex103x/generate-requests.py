#!/usr/bin/env python2

import sys
import random
from datetime import datetime
from datetime import timedelta

number_of_lines = 5000
rooms = [
    "normal_room",
    "double_room",
    "deluxe_room",
    "conference_room"
]

def main(args):
    for filename in args:
        request_id = 0
        with open(filename, "w+") as f:
            for i in range(0, number_of_lines):
                request_id += 1
                client_name = "foo bar"
                room_type = random.choice(rooms)
                request_type = "foorequest"
                start_date = datetime.today().date()
                end_date = datetime.today().date() + timedelta(random.randint(1, 7))
                num_adults = random.randint(1, 5)
                num_children = random.randint(1, 5)
                f.write("{}|{}|{}|{}|{}|{}|{}|{}\n".format(request_id, client_name,
                    room_type, request_type, start_date, end_date, num_adults,
                    num_children))

if __name__ == "__main__":
    random.seed()
    main(sys.argv[1:])
