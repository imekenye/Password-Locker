import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Arguments:
        unittest.TestCase: Testcase class that helps in creating cases
    """

    def setUp(self):
        """"
        Set up method to run before each test cases
        """
        self.new_user = User("John", "2468")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "John")
        self.assertEqual(self.new_user.password, "2468")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
        the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []



if __name__ == '__main__':
    unittest.main()
