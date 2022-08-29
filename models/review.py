#!/usr/bin/env python3
"""
This module contains the Review class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance from a dictionary.
        Args:
            *args (any): Not used for this project
            **kwargs (dict): Accepts var len of keyword args as attributes
        """
        super().__init__()

        if kwargs:
            for k, v in kwargs.items():
                if k in ["place_id", "user_id", "text"]:
                    self.__dict__[key] = v

