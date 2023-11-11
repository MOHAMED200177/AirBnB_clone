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

    def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id."""

        args = arg.split()

        if args == []:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return

        all_object = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in all_object.keys():
            all_object.pop(key)
            storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
