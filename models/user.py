#!/usr/bin/python3
""" Class user definition """
from models.base_model import BaseModel


class User(BaseModel):
    """ class user.

    attributes:
        email (str): user email
        password (str): user password
        first_name (str): user first name
        last_name (str)": user last name
    """
    email = ""
    passowrd = ""
    first_name = ""
    last_name = ""
