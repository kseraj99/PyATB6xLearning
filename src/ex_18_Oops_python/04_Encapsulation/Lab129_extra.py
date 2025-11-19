from dotenv import load_dotenv
import os


class VWOLogingPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        load_dotenv()
        if self.email == os.getenv("API_USERNAME") and self.password == os.getenv("API_PASSWORD"):
            print("Allowed to login")
        else:
            print("Login failed")

email = input("Enter the email:\n")
password = input("Enter the password:\n")

vwo_object_ref = VWOLogingPage(email, password)

vwo_object_ref.login_confirmation()

# from dotenv import load_dotenv
# import os
#
# class VWOLoginPage:
#
#     # Constructor to initialize email and password
#     def __init__(self, email_arg, password_arg):
#         self.email = email_arg
#         self.password = password_arg
#
#     # Method to verify login using .env credentials
#     def login_confirmation(self):
#         load_dotenv()  # Load variables from .env file
#
#         # Fetch environment variables
#         saved_username = os.getenv("API_USERNAME")
#         saved_password = os.getenv("API_PASSWORD")
#
#         # Debug (optional): Show loaded values
#         print("Loaded USERNAME:", repr(saved_username))
#         print("Loaded PASSWORD:", repr(saved_password))
#
#         # Compare user input with .env stored values
#         if self.email == saved_username and self.password == saved_password:
#             print("Allowed to login")
#         else:
#             print("Login failed")
#
#
# # ------ Main Program ------
#
# # Take input from the user
# email = input("Enter the email:\n")
# password = input("Enter the password:\n")
#
# # Create object from class
# vwo_object_ref = VWOLoginPage(email, password)
#
# # Call login confirmation
# vwo_object_ref.login_confirmation()

