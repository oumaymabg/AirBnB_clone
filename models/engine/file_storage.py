#!/usr/bin/python3
"""storage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ holder """
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f)
        f.close()

    def reload(self):
        """ holder """
        idclasses = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
        data = {}
        if(os.stat(self.__file_path).st_size is not 0):
            with open(self.__file_path) as json_file:
                data = json.load(json_file)
                for key, value in data.items():
                    self.__objects[key] = idclasses[value
                                  ['__class__']](**value)
