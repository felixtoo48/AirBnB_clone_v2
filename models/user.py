#!/usr/bin/python3
""" User class module that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """A subclass of BaseModel class
    Public class attribute:
        name: (str)
        password: (str)
        first_name: (str)
        last_name: (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
