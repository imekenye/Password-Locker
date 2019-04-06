#!/usr/bin/env python3.6
from user import User
from credential import Credential


def create_user(name, passw):
    """
    Function to create a new user
    """
    new_user = User(name, passw)
    return new_user


def create_credential(name, passw, email):
    """
    Function to create new user credentials
    """

    new_credential = Credential(name, passw, email)
    return new_credential


def save_users(user):
    """
    Function to save user
    """
    user.save_user()


def save_credentials(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete credentials
    """
    credential.delete_credential()


def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credential()


def generate_password(User):
    """
    Function that generates random passwords
    """
    return User.generate_pass()
