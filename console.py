#!/usr/bin/python3
"""console module
"""

import cmd
import shlex
import os
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class of command interpreter."""

    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit command to exit the program.")

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it"""
        if arg == "":
            print("** class name missing **")
            return
        else:
            try:
                myclass = eval(arg + "()")
                myclass.save()
                print(myclass.id)
            except Exception as e:
                print("** class doesn't exist **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
