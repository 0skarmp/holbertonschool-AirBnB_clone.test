#!/usr/bin/python3
import json
import os


class FileStorage:
    def __init__(self):
        """this is a class filestorgare"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """this a method all"""
        return self.__objects

    def new(self, obj):
        """this a method new that generate a new isntance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """this method serealized the dictionary in JSON"""
        dic_serialized = {}
        for key, value in self.__objects.items():
            dic_serialized[key] = value

        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(dic_serialized, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = f.read()
            self.__objects = json.loads(data)

            new_dict = {}

            for key, value in self.__objects.items():
                new_dict[key] = value
        else:
            pass
