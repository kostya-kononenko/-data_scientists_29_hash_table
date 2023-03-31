import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.valid_password(password)

    @staticmethod
    def valid_password(password):
        correct_length = False
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special_symbol = False
        if len(password) >= 7:
            correct_length = True
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
            if ch in "!@#$%^&*()_+":
                has_special_symbol = True
        if correct_length and has_uppercase and has_lowercase and has_digit and has_special_symbol:
            print("The password is correct")
            return hashlib.sha256(password.encode()).hexdigest()
        else:
            print("The password is not correct. The password \n"
                  "must be at least 7 characters long and contain at \n"
                  "least one uppercase letter, one lowercase letter \n"
                  "and one special character like !@#$%^&*()_+")


class AddingAndAuthorizingUser:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def create_hash(self, key):
        return hash(key) % self.size

    def add_user(self, user):
        index = self.create_hash(user.username)
        for some_user in self.table[index]:
            if some_user.username == user.username:
                raise ValueError("A user with that name already exists")
        self.table[index].append(user)

    def verify_user(self, username, password):
        index = self.create_hash(username)
        for some_user in self.table[index]:
            if some_user.username == username and some_user.password == \
                    hashlib.sha256(password.encode()).hexdigest():
                return True
        return False

    def interactive_login(self):
        username = input("Username: ")
        password = input("Password: ")
        if self.verify_user(username, password):
            print("User logged in successfully")
        else:
            print("Uncorrected password or user name, please try again")
