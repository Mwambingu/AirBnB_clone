#!/usr/bin/env python3
"""
Contains the BaseModel class. 
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes an instance of Base Model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at

    def save(self):
        """Stamps update time and saves a new object"""
        self.updated_at = datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """Coverts an object to a dictionary"""
        c_at = self.created_at.isoformat()
        u_at = self.updated_at.isoformat()
        self_d = self.__dict__
        self_d["__class__"] = __class__.__name__
        self_d["created_at"] = c_at
        self_d["updated_at"] = u_at
        return self.__dict__

    def __str__(self):
        """Returns the string representation of an object"""
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
