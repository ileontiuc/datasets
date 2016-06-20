#!/usr/bin/env python2

import sys
import random

import generate_bookings
import data

filename = "services.csv"

def main(args):
    bookings = ""
    with open(generate_bookings.filename, "r") as f:
        bookings = f.readlines()
    with open(filename, "w+") as f:
        f.write("booking id|price|description|date\n")
        for booking in bookings[1:]:
            parts = booking.split("|")
            room_prefix = parts[1][0]
            takes_service = random.random() < 0.6
            if takes_service: 
                booking_id = parts[0]
                index = int(0.5 + random.triangular(0, len(data.services.keys()) - 1))
                service = data.services.keys()[index]
                price = data.services[service]
                date = data.random_date_between_string(parts[2], parts[3])
                if room_prefix not in ["S", "L"] and "amusement" in service:
                    continue
                f.write("{}|{}|{}|{}\n".format(booking_id, price, service, date))

if __name__ == "__main__":
    random.seed(0)
    main(sys.argv[1:])

