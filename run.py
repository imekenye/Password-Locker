#!/usr/bin/env python3.6
from user import User
from credential import Credential
from random import *


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


def generate_password(num):
    """
    Function that generates random passwords
    """
    for i in range(num):
        return randint(0, 100)


def main():
    print("Welcome.What is your name?")
    myName = input()

    print(f"Hello {myName}!")
    print('\n')

    while True:
        print("Type in a number according to what you would want to do:\n 1 - Create account \n 2 - Log In")
        chosen = int(input())
        print('\n')

        if chosen == 1:
            print("Enter username:")
            uName = input()
            print("Do you want to auto generate a password? Y/N ")
            while True:
                answr = input().upper()
                if answr == 'Y':
                    userPass = generate_password(10)
                    print(f"This is your password - {userPass}")
                    break
                elif answr == 'N':
                    print("Enter your password for the account")
                    userPass = input()
                    print(f"This is your password - {userPass}")
                    break
                else:
                    print("please choose Y or N")


            save_users(create_user(uName, userPass))
            print('\n')
            print(f"Your new Username is --- {uName}")
            print('\n')

        elif chosen == 2:
            print("Please enter username?")
            uName = input()
            print("Password please?")
            userPass = input()

            if not User.user_list:  # check if list is empty
                print('\n')
                print("Sorry we do not have you in our list!")

            for user in User.user_list:

                if uName == user.username and userPass == user.password:
                    print("Login Success!!")
                    print('\n')

                    print(f"Welcome {uName}")

                    while True:
                        print(
                            "Choose number according to your needs: 1 - create new credential \n 2 - Display Credentials \n 3 - delete user")

                        chosenOne = int(input())

                        if chosenOne == 1:
                            print("Enter username")
                            usName = input()
                            print("Enter email")
                            mailName = input()
                            print("Auto-generate password? Y/N")
                            while True:
                                answer = input().upper()
                                if answer == 'Y':
                                    passwrd = generate_password(8)
                                    print(
                                        f"Your password is - {passwrd}")
                                    break
                                elif answer == 'N':
                                    print("Enter password")
                                    credentialpass = input()
                                    print(
                                        f"Your Password is - {credentialpass} ")
                                    break
                                else:
                                    print(
                                        "You have to choose something..here we go again Y/N")
                            credentialpass = input()
                            save_credentials(create_credential(
                                usName, mailName, credentialpass))

                            print('\n')
                            print(f"Credentials saved!")
                            print('\n')
                        elif chosenOne == 2:
                            if display_credentials():
                                print('\n')

                                for credential in display_credentials():
                                    print(
                                        f"{myName}'s credentials:- \n {credential.username} - {credential.email} - { credential.password}")
                                    print('\n')
                            else:
                                print("No user credentials!")
                                print('\n')
                        elif chosenOne == 3:
                            print("")


if __name__ == '__main__':

    main()
