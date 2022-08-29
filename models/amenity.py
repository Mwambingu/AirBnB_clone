#!/usr/bin/env python3
"""
Contains the Amenity module
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    name = ""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance from a dictionary.
        Args:
        *args (any): Not used for this project
        **kwargs (dict): Accepts var len of keyword args as attributes
        """
        super().__init__()

        if kwargs:
            for k, v in kwargs.items():
                if k == "name":
                    self.__dict__[k] = v
