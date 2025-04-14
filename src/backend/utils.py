from dotenv import load_dotenv
import os

class Utils:
    '''
    Classe que para metodos uteis. 
    Método: 
        db_url: Retorna a string do banco de dados "SQLALCHEMY_DATABASE_URL".'''
    _ = load_dotenv()
    @staticmethod
    def db_url():
        return os.getenv('SQLALCHEMY_DATABASE_URL')