#!/usr/bin/python3
'''
User class that inherits from BaseModel - useag still knwon
'''


from models.base_model import BaseModel


class User(BaseModel):
    '''
    Public class attributes
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
