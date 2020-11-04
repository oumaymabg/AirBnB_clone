#!/usr/bin/python3
"""holder"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
"""holder"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        exit()

    def do_EOF(self, arg):
        "Quit command to exit the program\n"
        exit()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
