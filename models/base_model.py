#!/usr/bin/python3
"""base class
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ base Object
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if (kwargs is not None):
            for key, value in kwargs.items():
                if key is ("created_at" or "updated_at"):
                    Date_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    self.__dict__[key] = Date_obj
                else:
                    self.__dict__[key] = value

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        new = self.__dict__.copy()
        new['class'] = self.__class__.__name__
        new['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new