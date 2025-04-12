from dotenv import load_dotenv
import os

class Utils:
    _ = load_dotenv()
    @staticmethod
    def db_url():
        return os.getenv('SQLALCHEMY_DATABASE_URL')