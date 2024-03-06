#!/usr/bin/python3
""" Review class def """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class

    attributes:
        place_id (str): place if
        user_id (str): user id
        text (str): user review text
    """

    place_id = ""
    user_id = ""
    text = ""
