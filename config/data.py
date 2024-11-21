import os

from dotenv import load_dotenv

load_dotenv()

class Data:

    LOGIN_STANDARD = os.getenv("LOGIN_STANDARD")
    PASSWORD_STANDARD = os.getenv("PASSWORD_STANDARD")

    LOGIN_ERROR = os.getenv("LOGIN_ERROR")
    PASSWORD_ERROR = os.getenv("PASSWORD_ERROR")

    LOGIN_PROBLEM = os.getenv("LOGIN_PROBLEM")
    PASSWORD_PROBLEM = os.getenv("PASSWORD_PROBLEM")