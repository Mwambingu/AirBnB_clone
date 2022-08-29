#!/usr/bin/env python3
"""
Contains the HBNB Console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
from models import user

classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

class HBNBCommand(cmd.Cmd):
    """Defines the HBNB CLI
    Attributes:
        prompt (str): the command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command to quit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an emptyline"""
        pass
    
    def do_create(self, arg):
        """Usage:  Creates a new instance based on a class
        ex: create BaseModel
        output: <instance id> b2947ae0-ff20-4ca2-a9ca-6ef101eac2be
        """
        if arg in classes:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Usage:  Prints all created instances or from a specified class
        ex: all <class name>
        output: [<class.name>] (<instance.id>) {<instance>}
        """
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
            else:
                for v in storage.all().values():
                    if arg == v.__class__.__name__:
                        print(v)
        else:
            for v in storage.all().values():
                print(v)
    
    def do_show(self, arg):
        """Usage:  Represents an instance based on class name and id.
        ex: show BaseModel 49faff9a-6318-451f-87b6-910505c55907
        output: [<class.name>] (<instance.id>) {<instance>}
        """
        arg_list = arg.split(" ")
        
        if not arg:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist  **")
        elif len(arg_list) < 2:
            print("** Instance id missing **")
        else:
            list_obj = storage.all()
            list_obj_keys = []
            obj_name = arg_list[0] + arg_list[1]
            for k in list_obj.keys():
                list_obj_keys.append(k)

            if obj_name in list_obj_keys:
                print(list_obj[obj_name])
            else:
                print("no instance found!!")
    
    def do_destroy(self, arg):
        """Usage:  Deletes an instance based on class name and id
        ex: destroy BaseModel 1234-1234-1234
        """
        arg_list = arg.split (" ")

        if not arg:
            print("** class name missing  **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** Instance id missing  **")
        else:
            obj_name = arg_list[0] + arg_list[1]
            list_obj_keys = []

            print("*** Keys Before deletion!! ***")
            for keys in storage.all().keys():
                print(keys)
                list_obj_keys.append(keys)
            if obj_name in list_obj_keys:
                del storage.all()[obj_name]
                storage.save()
            else:
                print("** Instance does not exist **")

            print("*** Keys After deletion!! ***")
            for keys in storage.all().keys():
                print(keys)
            
    def do_update(self, arg):
        """Usage:  Updates an instance based on the class and the id.
        ex: update BaseModel 1234-1234-1234 email 'aibnb@mail.com'"""

        arg_list = arg.split(" ")
        list_of_obj = storage.all()
        all_objs = []
        obj_attr = []
        obj_ids  = []

        for v in list_of_obj.values():
            all_objs.append(v.__dict__)

        for v in list_of_obj.values():
            obj_ids.append(v.id)

        for k in all_objs[0].keys():
            obj_attr.append(k)


        first_checks = False

        if not arg:
            print("** class name missing **")
        elif arg_list[0] not in classes:
            print("** class doesn't exist  **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[1] not in obj_ids:
            print("** no instance found **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            first_checks = True

        if first_checks:
            obj_name = arg_list[0] + arg_list[1]
            obj = list_of_obj[obj_name]
            setattr(obj, arg_list[2], arg_list[3])
            obj.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
