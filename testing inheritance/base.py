from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
    
    def __str__(self):
        c_name = self.__class__.__name__
        return "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
    
    def to_dict(self):
        """Coverts an object to a dictionary"""
        self_d = self.__dict__.copy()
        self_d["__class__"] = self.__class__.__name__
        self_d["created_at"] = self.created_at.isoformat()
        return self_d


#new_class = BaseModel()
#print(new_class)

#obj_dict = {
        #"id": "b7415ed3-48a0-4da1-afed-49cc7aa08256",
       # "created_at": "2022-08-24T20:25:50.018811",
       # }
#new_class = BaseModel(**obj_dict)
#print(new_class)