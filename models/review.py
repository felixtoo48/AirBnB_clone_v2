#!/usr/bin/python3
""" Review class module that inherits from
BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A subclass of BaseModel class
    Public class attribute:
        place_id: (str)
        user_id: (str)
        text: (str)
    """

    place_id = ""
    user_id = ""
    text = ""
