#!/usr/bin/python3
import json
import os


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
        new_dictionay = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for k, v in self.__objects.items():
                new_dictionary[key] = v.to_dict()
            dict_JSON = json.dumps(FileStorage.__objects)
            f.write(dict_JSON)
        
            
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            from models.base_model import BaseModel
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
