#!/usr/bin/python3
"""base class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City Object
    """
    state_id = ""
    name = ""
