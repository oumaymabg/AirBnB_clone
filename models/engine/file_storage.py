#!/usr/bin/python3
"""storage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ storage Object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ holder """
        return self.__objects

    def new(self, obj):
        """ holder """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ holder """
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)
        f.close()

    def reload(self):
        """ holder """
        idclasses = {'BaseModel': BaseModel}
        data = {}
        if(os.stat(self.__file_path).st_size is not 0):
            with open(self.__file_path) as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    self.__objects[key] = idclasses[value['__class__']](value)
