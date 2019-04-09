import random


class Credential:
    """
    Class that creates new instance of credentials
    """
    credential_list = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves credentials objects into credential_list    
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credentials list
        """
        return cls.credential_list
