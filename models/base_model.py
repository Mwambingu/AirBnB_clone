#!/usr/bin/env python3
"""
Contains the BaseModel class. 
"""
from uuid import uuid4
from datetime import datetime

class BaseMode:
    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.today().isoformat()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"[<{__class__.__name__}>] (<{self.id}>) <{self.__dict__}>"
