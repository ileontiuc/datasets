#!/usr/bin/env python2

import sys
import random
from datetime import datetime
from datetime import timedelta
from faker import Faker

# Local files
import data

filename = "requests.csv"

number_of_lines = 5000
def main(args):
    request_id = 0
    fake = Faker()
    fake.seed(0)
    with open(filename, "w+") as f:
        f.write("request id|client name|room type|request type|start date|end date|#adults|#children\n")
        for i in range(0, number_of_lines):
            request_id += 1
            client_name = fake.name()
            room_type = random.choice(data.rooms.keys())
            request_type = random.choice(["wedding", "party", "conference"]) if "conference" in room_type else random.choice(["holiday", "business"])
            start_date = data.random_date_between(datetime(2016, 1, 1).date(), datetime(2016, 3, 31))
            end_date = start_date + timedelta(1 + int(random.gammavariate(2, 2)))
            num_adults = max(1, int(random.betavariate(2, 5) * 10))
            num_children = int(random.betavariate(1, 5) * 10)
            if request_type == "conference":
                num_adults = max(1, int(random.normalvariate(25, 9)))
                num_children = 0
            elif request_type == "wedding":
                num_adults = max(2, int(random.normalvariate(25, 9)))
                num_children  = max(0, int(random.normalvariate(25, 12)))
            elif request_type == "party":
                num_adults = max(1, int(random.normalvariate(25, 9)))
                num_children  = max(0, int(random.normalvariate(25, 12)))
            elif request_type == "business":
                num_children /= 2
            f.write("{}|{}|{}|{}|{}|{}|{}|{}\n".format(request_id, client_name,
                room_type, request_type, start_date, end_date, num_adults,
                num_children))

if __name__ == "__main__":
    random.seed(0)
    main(sys.argv[1:])
