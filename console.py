#!/usr/bin/python3
import cmd
import sys
import json
from models.engine.file_storage import FileStorage


class idClasses:
    from models.base_model import BaseModel
    from models.user import User
    from models.engine.file_storage import FileStorage
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.place import Place
    from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        exit()

    def do_EOF(self, arg):
        "Quit the program when EOF\n"
        exit()

    def do_create(self, arg):
        "Holder\n"
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, arg)):
            print("** class doesn't exist **")
        else:
            targetClass = getattr(idClasses, arg)
            new = targetClass()
            new.save()
            print(new.id)

    def do_show(self, arg):
        "Holder\n"
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif (not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj = ['', '']
            for key in objs:
                obj = [objs[key].__class__.__name__, objs[key].id]
                if obj == args:
                    print(objs[key])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        "Holder\n"
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif (len(args) < 2):
            print("** instance id missing **")
        else:
            obj = ['', '']
            for key in objs:
                obj = [objs[key].__class__.__name__, objs[key].id]
                if obj == args:
                    del objs[key]
                    f.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        "Holder\n"
        f = FileStorage()
        f.reload()
        objs = f.all()
        ls = []
        if arg == "":
            for key in objs:
                ls.append(str(objs[key]))
            print(ls)
        elif(not hasattr(idClasses, arg)):
            print("** class doesn't exist **")
        else:
            for key in objs:
                cl = key.split(".")
                if cl[0] == arg:
                    ls.append(str(objs[key]))
            print(ls)

    def do_update(self, arg):
        "Holder\n"
        f = FileStorage()
        f.reload()
        objs = f.all()
        args = arg.split()
        if(arg == ""):
            print("** class name missing **")
        elif(not hasattr(idClasses, args[0])):
            print("** class doesn't exist **")
        elif(len(args) < 2):
            print("** instance id missing **")
        elif not(args[0]+"."+args[1] in objs):
                print("** no instance found **")
        elif (len(args) < 3):
            print("** attribute name missing **")
        elif (len(args) < 4):
            print("** value missing **")
        else:
            for key in objs:
                obj = key.split(".")
                if obj[0] == args[0] and obj[1] == args[1]:
                    value = objs[key]
                    setattr(value, args[2], args[3])
                    f.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
