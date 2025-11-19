
class VWOLogingPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirmation(self):
        if self.email == "serajkhan@gmail.com" and self.password == "1234":
            print("Allowed to login")
        else:
            print("Login failed")

email = input("Enter the email:\n")
password = input("Enter the password:\n")

vwo_object_ref = VWOLogingPage(email, password)

vwo_object_ref.login_confirmation()
