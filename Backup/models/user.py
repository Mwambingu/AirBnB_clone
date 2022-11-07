#!/usr/bin/env python3
"""
Contains the user module.
"""
from models.base_model import BaseModel

class User(BaseModel):

    def __init__(self, *args, **kwargs):
        """Initializes a new instance from a dictionary.
        Args:
        *args (any): Not used for this project
        **kwargs (dict): Accepts var len of keyword args as attributes
        """
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        if kwargs:
            for k, v in kwargs.items():
                if k in ["email", "password", "first_name", "last_name"]:
                    self.__dict__[k] = v
