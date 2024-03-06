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
            lex = split(arg[:brackets.span()[0]]
            ret = [i.strip(",") for i in lex]
            ret.append(brackets.group())
            return ret
    else:
        lex = split(arg[:braces.span()[0])
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
        match_arg = re.search(r"\.",arg)
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
        elif arg1[0] not int HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage : Show class id or <class>.show(<id>)
        """
        arg1 = parse_command(arg)
        obj_dict = storage.all()
        if len(arg1) ++ 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg1[0], arg1[1])])
































if __name__ == '__main__':
    HBNBCommand().cmdloop()
