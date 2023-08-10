from datetime import datetime

class CustomDate:
    def __init__(self):
        self.now = datetime.now()
    
    def get_date(self):
        return self.now.strftime("%d/%m/%Y")
    
    def get_time(self):
        return self.now.strftime("%H:%M:%S")

now = CustomDate()
print(now.get_date())
print(now.get_time())
