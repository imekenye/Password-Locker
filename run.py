#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(name, passw):
    """
    Function to create a new user
    """
    new_user = User(name, passw)
    return new_user
