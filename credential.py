class Credential:
    """
    Class that creates new instance of credentials
    """
    credential_list = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
