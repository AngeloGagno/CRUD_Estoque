from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import Utils

# Cria o motor do banco de dados, é o conecta com o banco
class Config:
    def __init__(self):
        self.engine = create_engine(Utils.db_url())

    def _start_session(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def engine_creator(self):
        return self.engine
    
    def get_db(self):
        SessionLocal = self._start_session()
        db = SessionLocal() 
        try:
            yield db
        finally:
            db.close()
