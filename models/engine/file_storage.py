#!/usr/bin/python3
""" Filestorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Storage File .

    attributes:
        __file_path (str): the name of the file
        __objects (dict): object representedin a dict.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return a dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ set obj with key """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """ serialise obj to JSON file"""
        obj_dict = FileStorage.__objects
        obj_dict = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as file_store:
            json.dump(obj_dict, file_store)

    def reload(self):
        """ deserialise the data in the json file"""
        try:
            with open(FileStorage.__file_path) as file_store:
                obj_dict = json.load(file_store)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
