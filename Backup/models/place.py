#!/usr/bin/env python3
"""
This module contains the Place Class
"""
from models.base_model import BaseModel

class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        """Initializes a new instance from a dictionary.
        Args:
            *args (any): Not used for this project
            **kwargs (dict): Accepts var len of keyword args as attributes
        """
        super().__init__()

        if kwargs:
            for k, v in kwargs.items():
                if k in ["city_id", "user_id", "name", "description", "amenity_ids"]:
                    self.__dict__[k] = v
                if k in ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]:
                    self.__dict__[k] = int(v)

       
