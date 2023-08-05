#!/usr/bin/python3
import json
import os


class FileStorage:
    """this is a class filestorgare"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this a method all"""
        return FileStorage.__objects

    def new(self, obj):
        """this a method new that generate a new isntance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()
        

    def save(self):
        """this method serealized the dictionary in JSON"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict_JSON = json.dumps(FileStorage.__objects)
            f.write(dict_JSON)

    def reload(self):
        from models.base_model import BaseModel


        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = f.read()
                JSON_dict = json.loads(data)

                for key, value in JSON_dict.items():
                    value = JSON_dict[key]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[key] = obj
        else:
            pass
