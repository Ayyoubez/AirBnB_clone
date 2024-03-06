#!/usr/bin/python3
""" Place class definition """
from models.base_model import BaseModel


class Place(BaseModel):
    """ class Place

    attributes:
        city_id (str): City id
        user_id (str): user id
        name (str): place name
        description (str): place description
        number_rooms (int): the number of the rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): place price
        latitude (float): place latitude
        longitude (float): place longitude
        amenity_ids (list): list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
