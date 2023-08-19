from datetime import *
class User:
    def __init__ (self,tk,mk):
        self.tk = tk
        self.mk = mk
    def welcome(self):
        return f'Welcome, {self.tk}'
    def check_password(self,mk):
        return self.mk == mk

class SubscribedUser(User):
    def __init__(self, username, password, expiration_date):
        super().__init__(username, password)
        self.expiration_date = expiration_date
    
    def is_expired(self):
        current_date = datetime.now()
        return current_date < self.expiration_date

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())
