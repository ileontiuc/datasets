#!/usr/bin/env python2

import sys
import random
import math
from datetime import datetime
from datetime import time

import data
import generate_bookings

filename = "food-orders.csv"

def calc_num_orders(num_people, days_of_stay):
    total = int(math.sqrt(num_people)) * days_of_stay / 10
    return random.randint(0, total)

def random_time_between(start, end):
    start_stamp = int(start.strftime("%s"))
    end_stamp = int(end.strftime("%s"))
    return datetime.fromtimestamp(random.randint(start_stamp, end_stamp)).date()

def random_room():
    room_type = random.choice(data.rooms.keys())
    return random.choice(data.rooms[room_type]["numbers"])

def room_type_from_prefix(prefix):
    for room in data.rooms.keys():
        if data.rooms[room]["prefix"] == prefix:
            return room

def select_dest_room(food_id, order_time, billed_room):
    food_category = data.menu[food_id]["category"]
    morning_start = time(6)
    morning_end = time(10)
    noon_start = time(11)
    noon_end = time(14)
    evening_start = time(18)
    evening_end = time(21)

    if food_category == "alcoholic-drink" and (order_time < time(14) or order_time > time(22)):
        return billed_room if random.random() < 0.8 else "restaurant"
    if food_category == "breakfast" and morning_start < order_time and order_time < morning_end:
        return "restaurant" if random.random() < 0.8 else billed_room
    if food_category == "lunch" and noon_start < order_time and order_time < noon_end:
        return "restaurant" if random.random() < 0.8 else billed_room
    if food_category == "dinner" and evening_start < order_time and order_time < evening_end:
        return "restaurant" if random.random() < 0.8 else billed_room

    return "restaurant" if random.random() < 0.6 else billed_room 

def main(args):
    with open(generate_bookings.filename, "r") as bookings, open(filename, "w+") as f:
        f.write("dest room|bill room|date|time|#orders|menu id\n")
        for booking_line in bookings.readlines()[1:]:
            booking_parts = booking_line.split("|")
            room = room_type_from_prefix(booking_parts[1][0])
            room_capacity = data.rooms[room]["capacity"]
            start_date = datetime.strptime(booking_parts[2], "%Y-%m-%d")
            end_date = datetime.strptime(booking_parts[3], "%Y-%m-%d")
            booked_time = end_date - start_date
            num_orders = calc_num_orders(room_capacity, booked_time.days)
            for i in range(num_orders):
                bill_dest = booking_parts[1]
                date = random_time_between(start_date, end_date)
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                time_ = time(hour, minute)
                num_servings = random.randint(1, 5)
                menu_id = random.choice(data.menu.keys())
                food_dest = select_dest_room(menu_id, time_, bill_dest)
                f.write("{}|{}|{}|{}|{}|{}\n".format(food_dest, bill_dest, date, time_, num_servings, menu_id))

if __name__ == "__main__":
    random.seed(0)
    main(sys.argv[1:])
