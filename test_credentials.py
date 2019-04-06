import unittest
from credential import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours

    Arguments:
        unittest.Testcase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("username", "password", "email")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.username, "username")
        self.assertEqual(self.new_credential.password, "password")
        self.assertEqual(self.new_credential.email, "email")

    def test_save_cred(self):
        """
        test_save_cred test case to test if the credential object is saved into the credentials list
        """

        self.new_credential.save_credential()  # save new credential
        self.assertEqual(len(Credential.credential_list), 1)


if __name__ == '__main__':
    unittest.main()
