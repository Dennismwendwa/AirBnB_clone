#!/usr/bin/python3
"""This is the class HBNBCommand for the entry point to interpreter"""

import cmd
import models

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """this is the command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """
        This method gets called at the EOF
        to exit
        """
        print()
        return True

    def emptyline(self):
        """This method gets called when emptyline is called"""
        pass

    def help_quit(self):
        """This is help message for quit"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        nw_instance = eval(args[0])()
        nw_instance.save()
        print(nw_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <instance id>
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = "{}.{}".format(args[0], args[1])

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        Usage: destroy <class name> <instance id>
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Args:
            arg (str): Class name
        """

        objects = models.storage.all()
        if not arg:
            print([str(objects[key]) for key in objects])
        elif arg in models.classes:
            filtered_obj = []
            for key in objects:
                if key.startswith(arg + "."):
                    filtered_obj.append(str(objects[key]))
            print(filtered_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        Usage: update <class name> <instance id> <attribute name>
        "<attribute value>"
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing *")
            return

        objects = models.storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        objects = models.storage.all()[key]
        attribute_name = args[2]
        attribute_value = args[3]

        if len(args) > 4:
            for arg in args[3:]:
                attribute_value += " " + arg

        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]

        setattr(objects, attribute_name, attribute_value)
        objects.save()

    def default(self, arg):
        """This meathod breaks down args for passing"""

        if "." not in arg:
            return (cmd.Cmd.default(self, arg))

        class_group = arg.split(".")
        _class = class_group[0]

        conversions = {40: 32, 41: None, 34: None, 44: None}
        commds = (class_group[1].translate(conversions)).split(" ")
        commd = commds[0]
        commd = commd.strip()

        if commd == "count":
            counts = 0
            for ky in models.storage.all().keys():
                if _class == ky.split(".")[0]:
                    counts += 1
            print(counts)
        elif commd == "show":
            _id = commds[1]
            self.do_show(_class + " " + _id)

        elif commd == "destroy":
            _id = commds[1]
            self.do_destroy(_class + " " + _id)
        elif commd == "all":
            self.do_all(_class)
        elif commd == "update":
            if len(commds) < 2:
                print("** instance id missing **")
                return
            elif len(commds) < 3:
                print("** attribute name missing **")
                return
            elif len(commds) < 4:
                print("** value missing **")
                return
            _id_no = commds[1]
            keys = commds[2]
            value = commds[3]
            self.do_update(_class + " " + _id_no + " " + keys + " " + value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
