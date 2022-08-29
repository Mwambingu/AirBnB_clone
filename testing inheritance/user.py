from base import BaseModel
from datetime import datetime

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
        
                    
obj_dict = {
        "id": "b7415ed3-48a0-4da1-afed-49cc7aa08256",
        "created_at": "2022-08-24T20:25:50.018811",
        "email": "kk_k@k_klan.com",
        "password": "blacklivesmatter",
        "first_name": "black",
        "last_name": "lover"
        }

new_user = User(**obj_dict)
print(new_user)

print(new_user.to_dict())