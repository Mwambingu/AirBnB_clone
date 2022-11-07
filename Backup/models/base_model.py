#!/usr/bin/env python3
"""
This module contains BaseModel class
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the BaseModel of the project.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance from a dictionary.
        Args:
            *args (any): Not used for this project
            **kwargs (dict): Accepts var len of keyword args as attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Stamps update time and saves a new object"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Coverts an object to a dictionary"""
        self_d = self.__dict__.copy()
        self_d["__class__"] = self.__class__.__name__
        self_d["created_at"] = self.created_at.isoformat()
        self_d["updated_at"] = self.updated_at.isoformat()
        return self_d

    def __str__(self):
        """Returns the string representation of an object"""
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
