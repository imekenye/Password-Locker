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

if __name__ == '__main__':
    unittest.main()
