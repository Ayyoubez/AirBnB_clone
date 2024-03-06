#!/usr/bin/python3
""" City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class City

    attributes:
    state_id (str): state id of the city
    name (str): City name
    """

    state_id = ""
    name = ""
