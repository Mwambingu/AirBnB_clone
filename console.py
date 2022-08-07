#!/usr/bin/env python3
"""
Contains the HBNB Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB CLI
    Attributes:
        prompt (str): the command prompt.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command to quit the program"""
        return True

    def do_EOF(self, art):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an emptyline"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
