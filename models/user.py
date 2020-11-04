#!/usr/bin/python3
"""base class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ user Object
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
