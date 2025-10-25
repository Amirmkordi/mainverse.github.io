import re
import string
from colorama import Fore
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
class Login:
    def __init__(self):
        self.users = []
        self.load()

    def load(self):
        try:
            f = open("RayDB.txt", mode="r")
            users = f.readlines()
        except:
            f = open("RayDB.txt", mode="w")
            users = list()
        for u in users:
            tmp = u.split(" ")
            self.users.append(User(tmp[0],tmp[1]))

    def save(self):
        with open("UserDB.txt", "w") as f:
            for u in self.users:
                f.write(u.username + " " + u.password + "\n")
    
    def long_enough(self,pw):
        return len(pw) >= 8

    def has_lowercase(self,pw):
        return len(set(string.ascii_lowercase).intersection(pw)) > 0

    def has_uppercase(self,pw):
        return len(set(string.ascii_uppercase).intersection(pw)) > 0

    def has_numeric(self,pw):
        return len(set(string.digits).intersection(pw)) > 0

    def has_special(self,pw):
        return len(set(string.punctuation).intersection(pw)) > 0

    def password_checker(self,pw, tests=[long_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
        for test in tests:
            if not test(self,pw):
                print("Your password is not strong enough !!!")
                return False
        return True
    
    def email_checker(self,email):
        pattern= '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        result = re.search(pattern, email)
        if result == False:
            print("Invalid email address. Please enter a valid email address.")
            return False
    def signup(self):
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if self.password_checker(pwd)== False :
            return False
        if self.email_checker(email) == False:
            return False
        elif conf_pwd == pwd:
            self.users.append(User(email, pwd))
            print("You have registered successfully!")
            return True
        print("Passwords do not match!")
        return False

    def login(self):
        email = input("Enter email: ")
        self.email = email
        pwd = input("Enter password: ")
        for u in self.users:
            if email == u.username and pwd == u.password:
                print("Logged in successfully!")
                return email
        print("Wrong username or password")
        return None

    def run(self):
        while True :
            print(Fore.RED + " --------------")
            print(Fore.RED + "-- Login System --")
            print(Fore.RED + "1. Signup")
            print(Fore.RED + "2. Login")
            print(Fore.RED + "------------------")
            print(Fore.RED + " --------------")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                self.signup()
                self.save()
            elif ch == 2:
                return self.login()
            else:
                print("Wrong Choice! Try again")