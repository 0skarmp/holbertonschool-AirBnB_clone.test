#!/usr/bin/python3
"""
this console define a "airBnB" console.
"""
import cmd
import sys
from models import storage
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
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """ show the class name and id """
        class_id = arg.split()
        if not class_id:
            print("** class name missing **")

        elif class_id[0] not in HBNBCommand.l_class:
            print("** class doesn't exist **")

        elif len(class_id) < 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(class_id[0], class_id[1])
            all_objects = storage.all()

            if key not in all_objects:
                print("** no instance found **")

            else:
                print(f"{all_objects[key]}")

    def do_destroy(self, arg):
        """ delete an instacne based on the class name and id"""
        class_id = arg.split()
        if not class_id:
            print("** class name missing **")

        elif class_id[0] not in HBNBCommand.l_class:
            print("** class doesn't exist **")

        elif len(class_id) < 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(class_id[0], class_id[1])
            all_objects = storage.all()

            if key not in all_objects:
                print("** no instance found **")

            else:
                del all_objects[key]
                storage.save()

    def do_all(self, arg):
        if not arg:
            print([str(v) for v in storage.all().values()])
        else:
            class_id = arg.split()
            data = []
            all_objects = storage.all()

            for obj in all_objects.values():
                if type(obj).__name__ == class_id[0]:
                    data.append(str(obj))
            print(data)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        class_id = arg.split()
        if not class_id:
            print("** class name missing **")
        elif class_id[0] not in HBNBCommand.l_class:
            print("** class doesn't exist **")
        elif len(class_id) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_id[0], class_id[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            elif len(class_id) < 3:
                print("** attribute name missing **")
            elif len(class_id) < 4:
                print("** value missing **")
            else:
                attribute_name = class_id[2]
                attribute_value = class_id[3]

                obj = all_objects[key]
                setattr(obj, attribute_name, attribute_value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
