#!/usr/bin/python3
"""storage class
"""


import json
import os


class FileStorage:
    """ storage Object
    """
    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        open(self.__file_path, 'a')
        self.__objects = {}

    def all(self):
        """ holder """
        return self.__objects

    def new(self, obj):
        """ holder """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()
 
    def save(self):
        """ holder """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
        f.close()

    def reload(self):
        """ holder """
        if(os.stat(self.__file_path).st_size is not 0):
            with open(self.__file_path) as json_file: 
                self.__objects = json.load(json_file) 
