#!/usr/bin/python3
""" Amenity class module that inherits from
BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """

    name = ""
