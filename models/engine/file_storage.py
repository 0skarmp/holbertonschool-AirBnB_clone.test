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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """this method serealized the dictionary in JSON"""
        dic_serialized = {}
        for key, value in self.__objects.items():
            dic_serialized[key] = value

        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(dic_serialized, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects_data = json.load(f)
            for key, value in objects_data.items():
                class_name, obj_id = key.split(".")
                class_obj = eval(class_name)
                obj_instance = class_obj(**value)
                self.new(obj_instance)

        else:
            pass
