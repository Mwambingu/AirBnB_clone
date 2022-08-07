#!/usr/bin/env python3
"""
Contains the file storage class
"""
from models.base_model import BaseModel
import json

class FileStorage:
    """ The file storage class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects stored"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new instance to the object storage"""
        cls_id = "{}{}".format(__class__.__name__, obj.id)
        FileStorage.__objects[cls_id] = obj

    def save(self):
        """ Stores all objects to json to a json file"""
        odict = FileStorage.__objects
        objdict={}
        for obj_id, obj in odict.items():
            objdict[obj_id] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f, indent=4)

    def reload(self):
        """ Reloads all objects from json file"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for v in objdict.values():
                    new_obj = BaseModel(**v)
                    self.new(new_obj)
        except FileNotFoundError:
            return
