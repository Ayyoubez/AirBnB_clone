#!/usr/bin/python3
""" The HBnB console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter

    attributes:
        promt (str): the command promt
    """
    prompt = "(hbnb)"

    def do_quit(self):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Exit the console when receiving EOF"""
        print()
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
