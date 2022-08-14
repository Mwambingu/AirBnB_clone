#!/usr/bin/env python3
"""
Contains the HBNB Console
"""
import cmd
from models import base_model
from models import storage


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
        """Creates a new instance"""
        if arg == "BaseModel":
            new_instance = base_model.BaseModel()
            new_instance.save()
            print(new_instance.id)

        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Usage:  Represents an instance based on class name and id.
        ex: show BaseModel 49faff9a-6318-451f-87b6-910505c55907
        output: [<class.name>] (<instance.id>) {<instance>}
        """
        arg_list = arg.split(" ")
        
        if not arg:
            print("** class name missing **")
        elif "BaseModel" != arg_list[0]:
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
        elif "BaseModel" != arg_list[0]:
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
            
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
