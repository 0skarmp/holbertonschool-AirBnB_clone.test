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

        self.__objects[key] = obj        

    def save(self):
        """this method serealized the dictionary in JSON"""
        new_dictionary = {}
        
        for k, v in self.__objects.items():
            new_dictionary[k] = v.to_dict()
            
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(new_dictionary, file)  
            
    def reload(self):
        from models.base_model import BaseModel


        """Deserialize the JSON file __file_path to __objects, if it exists"""
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = f.read()
                JSON_dict = json.loads(data)

                for k, v in JSON_dict.items():
                    value = JSON_dict[k]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[k] = obj
        else:
            pass
