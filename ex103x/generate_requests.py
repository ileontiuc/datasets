#!/usr/bin/env python2

import sys
import random
from datetime import datetime
from datetime import timedelta
from faker import Faker

# Local files
import data

filename = "requests"

number_of_lines = 5000
def main(args):
    request_id = 0
    fake = Faker()
    with open(filename, "w+") as f:
        for i in range(0, number_of_lines):
            request_id += 1
            client_name = fake.name()
            room_type = random.choice(data.rooms.keys())
            request_type = random.choice(["wedding", "party", "conference"]) if "conference" in room_type else random.choice(["holiday", "business"])
            start_date = datetime.today().date() - timedelta(random.randint(0, 100))
            end_date = start_date + timedelta(random.randint(1, 14))
            num_adults = random.randint(1, 5)
            num_children = random.randint(1, 5)
            f.write("{}|{}|{}|{}|{}|{}|{}|{}\n".format(request_id, client_name,
                room_type, request_type, start_date, end_date, num_adults,
                num_children))

if __name__ == "__main__":
    random.seed(0)
    main(sys.argv[1:])
