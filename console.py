#!/usr/bin/python3
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    def do_quit(self, arg):
        "Quit command to exit the program"
        exit()
    def do_EOF(self, arg):
        "Quit the program when EOF"
        exit()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
