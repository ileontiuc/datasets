#!/usr/bin/env python2

import sys
import random
import math
from datetime import datetime
from datetime import timedelta

#Local files
import data
import generate_requests

requests_file_name = generate_requests.filename
filename = "bookings.csv"

class Booking:
    def __init__(self, booking_id, room_type, start_date, end_date, request_id):
        self.booking_id = booking_id
        self.room_type = room_type
        self.start_date = start_date
        self.end_date = end_date
        self.request_id = request_id
        self.room_no = None

    def __str__(self):
        return "{}|{}|{}|{}|{}".format(self.booking_id, self.room_no, self.start_date, self.end_date, self.request_id)

def main(args):
    bookings = {}
    unique_bookings = []
    booking_id = 0
    # Create 2D map of room requests
    with open(requests_file_name, "r") as requests_file:
        request_lines = requests_file.readlines()
        for request_line in request_lines[1:]:
            if random.random() < 0.05:
                continue
            request_line_parts = request_line.split("|")
            room_type = request_line_parts[2]
            num_people = int(request_line_parts[-1]) + int(request_line_parts[-2])
            room_capacity = data.rooms[room_type]["capacity"]
            num_rooms = int(math.ceil(float(num_people) / room_capacity))
            for _ in range(num_rooms):
                booking_id += 1
                start_date = datetime.strptime(request_line_parts[4], "%Y-%m-%d").date()
                end_date = datetime.strptime(request_line_parts[5], "%Y-%m-%d").date()
                request_id = request_line_parts[0]
                booking = Booking(booking_id, room_type, start_date, end_date, request_id)
                unique_bookings.append(booking)
                for days in range((end_date - start_date).days):
                    key = start_date + timedelta(days)
                    if key not in bookings:
                        bookings[key] = []
                    bookings[key].append(booking)

    # Assign rooms. No double bookings.
    for date in bookings.keys():
        unassigned = [x for x in bookings[date] if x.room_no == None]
        for booking in unassigned:
            taken_rooms = [x.room_no for x in bookings[date] if x.room_no != None]
            prefix = data.rooms[booking.room_type]["prefix"]
            num = 0
            room_no = "{}{}".format(prefix, num)
            while room_no in taken_rooms:
                num += 1
                room_no = "{}{}".format(prefix, num)
            booking.room_no = room_no

    with open(filename, "w") as f:
        f.write("id|room|start date|end date|request id\n")
        for booking in unique_bookings:
            f.write("{}\n".format(booking))                    

if __name__ == "__main__":
    random.seed(0)
    main(sys.argv[1:])
