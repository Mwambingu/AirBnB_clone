#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new Place --")
my_place = Place()
my_place.name = "Urban Furnished Apartment"
my_place.description = "A comfy two bedroom apartment with a balcony view of Kanairo."
my_place.my_number_rooms = 4
my_place.number_bathrooms = 1
my_place.max_guest = 2
my_place.price_by_night = 55
my_place.latitude = 55.34
my_place.longitude = 33.42
my_place.save()
print(my_place)


