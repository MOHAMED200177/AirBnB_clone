#!/usr/bin/python3
"""
This module defines the HBNBCommand class, which is a command interpreter
with specific functionality.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command interpreter that inherits from cmd.Cmd.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty input line (just pressing ENTER).
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit the program.
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
