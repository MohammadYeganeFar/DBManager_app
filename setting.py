import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
DB_DIR = pathlib.Path.joinpath(BASE_DIR, "apps", "database")
USERS_DB = pathlib.Path.joinpath(DB_DIR, "data", "users_data.json")

