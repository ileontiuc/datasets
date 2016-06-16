
import random
from datetime import datetime

rooms = {
    "normal_room": {
        "prefix": "N",
        "price": 80,
        "capacity": 1
    },
    "double_room": {
        "prefix": "D",
        "price": 100,
        "capacity": 3
    },
    "deluxe_room": {
        "prefix": "X",
        "price": 150,
        "capacity": 3
    },
    "conference_room_small": {
        "prefix": "S",
        "price": 80,
        "capacity": 15
    },
    "conference_room_large": {
        "prefix": "L",
        "price": 150,
        "capacity": 50
    }
}

menu = {
    0: {
        "name": "water",
        "price": 2.50,
        "category": "drink"
    },
    1: {
        "name": "soft-drink",
        "price": 3,
        "category": "drink"
    },
    2: {
        "name": "beer",
        "price": 3.50,
        "category": "alcoholic-drink"
    },
    3: {
        "name": "wine",
        "price": 3.50,
        "category": "alcoholic-drink"
    },
    4: {
        "name": "simple-breakfast",
        "price": 5,
        "category": "breakfast"
    },
    5: {
        "name": "french-breakfast",
        "price": 7,
        "category": "breakfast"
    },
    6: {
        "name": "deluxe-breakfast",
        "price": 12,
        "category": "breakfast"
    },
    7: {
        "name": "simple-lunch",
        "price": 5,
        "category": "lunch"
    },
    8: {
        "name": "deluxe-lunch",
        "price": 10,
        "category": "lunch"
    },
    9: {
        "name": "steak 'n stuff",
        "price": 18,
        "category": "dinner"
    },
    10: {
        "name": "surf 'n turf",
        "price": 17,
        "category": "dinner"
    },
    11: {
        "name": "vegetarian lasagna",
        "price": 16,
        "category": "dinner"
    },
    12: {
        "name": "spareribs",
        "price": 17,
        "category": "dinner"
    },
    13: {
        "name": "super soup",
        "price": 14,
        "category": "dinner"
    },
    14: {
        "name": "coffee",
        "price": 3,
        "category": "drink"
    },
    15: {
        "name": "tea",
        "price": 2.5,
        "category": "drink"
    }
}

services = {
        "decoration_party": 20,
        "decoration_flowers": 10,
        "decoration_romantic_flowers": 15,
        "amusement_clown": 100,
        "amusement_live_music": 100,
        "amusement_dj": 90
}

def random_date_between_string(start_date_string, end_date_string):
    start_date = datetime.strptime(start_date_string, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_string, "%Y-%m-%d")
    random_date_between(start_date, end_date)

def random_date_between(start_date, end_date):
    start_stamp = start_date.strftime("%s")
    end_stamp = end_date.strftime("%s")
    random_date = datetime.fromtimestamp(random.randint(int(start_stamp), int(end_stamp)))
    return random_date.date()

