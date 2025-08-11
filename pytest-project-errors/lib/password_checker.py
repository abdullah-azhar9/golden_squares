# File: lib/password_checker.py

class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")

#Test to see if True is returned when password greater than 8 chars.
#Test to see if Exception is returned when password less than 8 chars.