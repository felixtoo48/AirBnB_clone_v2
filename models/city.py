#!/usr/bin/python3
""" City class module that inherits from
BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """A subclass of BaseModel class
    Public class attribute:
        state_id: (str)
        name: (str)
    """

    state_id = ""
    name = ""
