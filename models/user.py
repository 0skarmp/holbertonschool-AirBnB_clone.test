#!/usr/bin/python3
"""
this module has a class that inherits form BaseModel
"""


from models.base_model import BaseModel


class User(BaseModel):
    """this define class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
