#!/usr/bin/python3
""" Module contains class BaseModel
Base class of all the classes in the project
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """initializes object using dictionary if given otherwise
        it gives default value
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ initialize str
        returns class name, id and the dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """ updates the public instance attributes
        update current date time
        invoke save function
        save to serialized file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """ returns dictionary containing all key value pairs
        of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        return dic
