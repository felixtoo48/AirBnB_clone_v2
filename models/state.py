#!/usr/bin/python3
""" State class module that inherits from
BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """A subclass of BaseModel class
    Public class attribute:
        name: (str)
    """

    name = ""
