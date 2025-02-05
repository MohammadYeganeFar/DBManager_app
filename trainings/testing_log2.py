import logging
logging.basicConfig(filename="users_data.log", level=logging.INFO, 
                    format="%(levelname)s:%(message)s:")

class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        logging.info(f"user added : name= {self.name}, email= {self.email}")

class OperationLog:
    @staticmethod
    def log_add(user):
        logging.info(f"Add operation: User {user.name} with email {user.email} added.")

    @staticmethod
    def log_update(user):
        logging.info(f"Update operation: User {user.name} with email {user.email} updated.")

    @staticmethod
    def log_delete(user):
        logging.info(f"Delete operation: User {user.name} with email {user.email} deleted.")

u1 = Users("mohammad", "mmdvafaj@gmail.com")
u2 = Users("mad", "vafaj@gmail.com")

OperationLog.log_add(u1)
OperationLog.log_update(u2)
OperationLog.log_delete(u1)


