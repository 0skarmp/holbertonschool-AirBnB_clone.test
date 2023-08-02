#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
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

        for k, v in data.items():
            class_name, obj_id = key.split(".")

        if class_name == "BaseModel":
            obj = BaseModel(**value)
            FileStorage.__object[key] = obj 
