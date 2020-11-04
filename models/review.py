#!/usr/bin/python3
"""base class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Amenity Object
    """
    place_id = ""
    user_id = ""
    text = ""
