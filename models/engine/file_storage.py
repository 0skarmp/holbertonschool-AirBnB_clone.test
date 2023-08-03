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
        FileStorage.__objects[key] = obj

    def save(self):
        """this method serealized the dictionary in JSON"""
        dic_serialized = {}
        for key, value in FileStorage.__objects.items():
            dic_serialized[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            json.dump(dic_serialized, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)

            for key, value in data.items():
                class_name, obj_id = key.split(".")

                if class_name == "BaseModel":
                    obj = BaseModel(**value)
                    FileStorage.__object[key] = obj
