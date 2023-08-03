#!/usr/bin/python3
import uuid
import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Sets the initial attributes of an instance of the class """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, formati)
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(selee)

    def __str__(self):
        """ __str__ special method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save method"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict method converts from object - dictionary """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
