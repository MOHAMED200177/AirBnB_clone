#!/usr/bin/python3
"""console module
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class of command interpreter."""

    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel, "User": User}

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
            print(all_object[key].__str__())

        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id.
        """
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

    def do_all(self, arg):
        """Print all string representation of all instances"""
        args = arg.split()

        objects_string_representation = []
        class_to_represent = None
        if args != []:
            class_to_represent = args[0]
            if class_to_represent not in self.classes:
                print("** class doesn't exist **")
                return

        objects_class = storage.all()
        for obj in objects_class.values():
            if class_to_represent is None:
                objects_string_representation.append(obj.__str__())
            elif obj.__class__.__name__ == class_to_represent:
                objects_string_representation.append(obj.__str__())

        print(objects_string_representation)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        ar_len = len(args)
        if args == []:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif ar_len < 2:
            print("** instance id missing **")
            return
        else:
            objects_class = storage.all()
            key = args[0] + "." + args[1]

            if key not in objects_class.keys():
                print("** no instance found **")
                return
            elif ar_len < 3:
                print("** attribute name missing **")
                return
            elif ar_len < 4:
                print("** value missing **")
                return
            else:
                setattr(objects_class[key],
                        args[2],  eval(args[3]))
                objects_class[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
