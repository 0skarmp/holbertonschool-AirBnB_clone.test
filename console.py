#!/usr/bin/python3
"""
this console define a "airBnB" console.
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    this class HBNB define
   the classes of the console.
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """  quit command to exit the program"""
        exit()
        return True

    def do_EOF(self, arg):
        """ EOF command 'end of the line' to exit the program"""
        exit()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
