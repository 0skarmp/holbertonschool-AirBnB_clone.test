#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """this is a class filestorgare"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this a method all"""
        return self.__objects

    def new(self, obj):
        """this a method new that generate a new isntance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """this method serealized the dictionary in JSON"""
        o_dct = {}

        for key, obj in self.__objects.items():
            o_dct[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(odct_dict, file)
            
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                read = f.read()
                book = json.loads(read)
                for k, v in book.items():
                    value = book[k]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[k] = obj
        else:
            pass
