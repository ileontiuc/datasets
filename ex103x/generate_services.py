#!/usr/bin/env python2

import sys
import random
from datetime import datetime

import generate_bookings
import data

filename = "services"

def random_date_between(start_date_string, end_date_string):
    start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_string, "%Y-%m-%d")
    start_stamp = start_date.strftime("%s")
    end_stamp = end_date.strftime("%s")
    random_date = datetime.fromtimestamp(random.randint(int(start_stamp), int(end_stamp)))
    return random_date.date()

def main(args):
    bookings = ""
    with open(generate_bookings.filename, "r") as f:
        bookings = f.readlines()
    with open(filename, "w+") as f:
        for booking in bookings:
            parts = booking.split("|")
            num_items = random.randint(0,1)
            room_prefix = parts[1][0]
            takes_service = random.random() < 0.6
            if takes_service: 
                booking_id = parts[0]
                service = random.choice(data.services.keys())
                price = data.services[service]
                date = random_date_between(parts[2], parts[3])
                if room_prefix not in ["S", "L"] and "amusement" in service:
                    continue
                f.write("{}|{}|{}|{}\n".format(booking_id, price, service, date))

if __name__ == "__main__":
    random.seed()
    main(sys.argv[1:])

