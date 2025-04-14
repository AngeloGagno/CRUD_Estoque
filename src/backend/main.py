from API.router import router
from database.database_conf import Config
from database.models import *
from fastapi import FastAPI

## Execução do backend ## 

Base.metadata.create_all(bind=Config().engine_creator()) # Caso a tabela não exista no banco, cria uma
app = FastAPI() 
app.include_router(router=router) # Crias as rotas da API