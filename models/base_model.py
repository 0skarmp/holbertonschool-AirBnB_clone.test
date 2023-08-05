#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models 


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Sets the initial attributes of an instance of the class """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    fdT = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.strptime(value, fdT)
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ __str__ special method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict method converts from object - dictionary """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = str(self.created_at.isoformat())
        dict_copy["updated_at"] = str(self.updated_at.isoformat())
        return dict_copy
