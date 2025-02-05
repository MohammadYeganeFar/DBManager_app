import json
import pathlib
import sys
from time import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from setting import USERS_DB
# Add the project root directory to Python path

# sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent.parent))


class DBManager:
    
    """
    # BY AI
    A class to handle database operations including reading, writing, and updating JSON data
    Implements Singleton pattern to ensure only one instance exists.
    """
    _instance = None
    def __new__(cls, file_path=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
            cls._instance._ensure_file_exists()
        return cls._instance
    
    def _ensure_file_exists(self) -> None:
        """Create the file and parent directories if they don't exist"""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        # parents = True :create dir if does not exist
        # exist_ok = dont get FileExistsError if the file exist
        if not self.file_path.exists():
            self.write_data({"users": []})

    def read_data(self) :
        """Read and return the JSON data from the file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {"users": []}

    def write_data(self, data) -> bool:
        """Write data to the JSON file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def add_user(self, user_data) -> bool:
        """Add a new user to the JSON file"""
        data = self.read_data()
        user_data["created_at"] = time()
        user_data["last_login"] = time()
        data["users"].append(user_data)
        return self.write_data(data)


    def get_user(self, username: str) :
        """Retrieve a user by username"""
        data = self.read_data()
        for user in data["users"]:
            if user["username"] == username:
                return user
        return None
    
    def delete_user(self, username: str) -> bool:
        """Delete a user from the JSON file"""
        data = self.read_data()
        data["users"] = [user for user in data["users"] if user["username"] != username]
        return self.write_data(data)



# tes singleton
db = DBManager(USERS_DB)
db2 = DBManager(USERS_DB)
print(db is db2)

# Example usage:
user_data = {
    "username": "ali",
    "password": "secure_password",
    "email": "new.user@example.com",
    "role": "user"
}
db.add_user(user_data)
