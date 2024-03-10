#!/usr/bin/python3
""" The HBnB console """
import cmd
import re
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse_command(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brackets.span()[0]])
            ret = [i.strip(",") for i in lex]
            ret.append(brackets.group())
            return ret
    else:
        lex = split(arg[:braces.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(braces.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter

    attributes:
        promt (str): the command promt
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the console when receiving EOF"""
        print("")
        return True

    def emplyline(self):
        """Do nothing with empty input"""
        pass

    def help_quit(self):
        """ Help message for Quit method"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """ Help message for EOF method"""
        print("Exit the console when receiving EOF")

    def default(self, arg):
        """ Default action when invalid input given"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match_arg = re.search(r"\.", arg)
        if match_arg is not None:
            arg1 = [arg[:match_arg.span()[0]], arg[mathc_arg.span()[1]:]]
            match_arg = re.search(r"\((.*?)\)", arg1[1])
            if match is not None:
                comd = [arg1[1][:match_arg.span()[0]], match_arg.group()[1:-1]]
                if comd[0] in arg_dict.keys():
                    call = "{} {}".format(arg1[0], comd[1])
                    return arg_dict[comd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Usage : Create <class>
        create a new object and print is ID
        """
        arg1 = parse_command(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage : Show class id or <class>.show(<id>)
        """
        arg1 = parse_command(arg)
        obj_dict = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg1[0], arg1[1])])

    def do_update(self, arg):
        """Usage: update an instance by a given id
        <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        arg1 = parse_command(arg)
        obj_dict = storage.all()

        if len(arg1) == 0:
            print("** class name missing **")
            return False
        if arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg1[0].arg1[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg1) == 4:
            obj = obj_dict["{}.{}".format(arg1[0], arg1[1])]
            if arg1[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[arg1[2]])
                abj.__dict__[arg[2]] = value_type(arg1[3])
            else:
                obj.__dict__[arg1[2]] = arg1[3]
        elif type(eval(arg1[2])) == dict:
            obj = obj_dict["{}.{}".format(arg1[0], arg1[1])]
            for key, value in eval(arg1[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {
                            str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_all(self, arg):
        arg1 = parse_command(arg)
        """Usage : prints all instances of a given class or
        display all the objects created
        """
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg1) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_count(self, arg):
        """ Usage : count or  retrieve the number of instances
        of a class: <class name>.count()
        """
        arg1 = parse_command(arg)
        count = 0
        for objects in storage.add().values():
            if arg1[0] == objects.__class__.__name__:
                count += 1
        print(count)

    def do_destroy(self, arg):
        """ Usage :  destroy an instance based on
        his ID: <class name>.destroy(<id>)
        """
        arg1 = parse_command(arg)
        obj_dict = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg1[0], arg1[1])]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
