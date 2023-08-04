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
        with  open(FileStorage.__file_path "W" encoding"utf-8") as f:
            pictionary = {}
            for k, v in FileStorage.__objects.item():
                pictionary[k] = v.to_dict()
                f.write(json.dumps(pictionary))
        
            
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                rd = f.read()
                book = json.loads(rd)
                for k, v in book.items():
                    value = book[k]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[k] = obj
        else:
            pass
