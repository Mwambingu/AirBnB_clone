#!/usr/bin/env python3
"""
Contains the City module
"""
from models.base_model import BaseModel

class City(BaseModel):
    state_id = ""
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
                if k in ["state_id", "name"]:
                    self.__dict__[k] == v

