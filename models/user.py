#!/usr/bin/python3
"""
this module has a class that inherits form BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """this define class User"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
