#!/usr/bin/python3
""" Base model class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class resentation """

    def __init__(self, *args, ***kwargs):
        """ BaseModel constructor

        Args:
            *args (dif): unused.
            **kwargs (dict): key/value as a dictionnary.
        """
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['crated_at', 'updated_at']:
                        val = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(slef):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
