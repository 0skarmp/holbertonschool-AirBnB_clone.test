#!/usr/bin/python3
"""
this console define a "airBnB" console.
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    this class ommand
   the classes of the console.
    """
    prompt = '(hbnb)'
    l_class = ['BaseModel']

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
    
    def do_create(self, arg):
        """Do created new instance of the class and print ID"""
        if not arg:
            print("** class name missing **")

        elif arg not in HBNBCommand.l_class: 
            print("** class doesn't exist **")
        
        else:
            dct = {'BaseModel': BaseModel}
            obj = dct[arg]()
            print(obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
