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

