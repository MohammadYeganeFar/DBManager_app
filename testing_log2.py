import logging
logging.basicConfig(filename="users_data.log", level=logging.INFO, 
                    format="%(levelname)s:%(message)s:")

class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        logging.info(f"user added : name= {self.name}, email= {self.email}")

u1 = Users("mohammad", "mmdvafaj@gmail.com")
u2 = Users("mad", "vafaj@gmail.com")
