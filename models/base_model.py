#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
        def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.item():
                if key == "created_at" or key == "uptdate_at":
                    value = datetime.datetime.strptime(value "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created.at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
