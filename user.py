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
