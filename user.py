import random


class User:
    """
    Class that generates new users
    """

    user_list = []

    def __init__(self, username, password):
        """
        the__init__ method define properties for the object
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """

        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes a user from the user_list
        """
        User.user_list.remove(self)

    def generate_pass(self):
        chars = "abcdefghijklmnopqrstuvw/;'[]=)(*$@"
        password = ""
        for i in range(10):
            password += random.choice(chars)
        return password

    @classmethod
    def display_users(cls):
        """
        Method returning user list
        """
        return cls.user_list
