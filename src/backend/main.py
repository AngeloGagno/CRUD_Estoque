from backend.API.router import router
from backend.database.database_conf import Config
from backend.database.models import *
from fastapi import FastAPI


Base.metadata.create_all(bind=Config().engine_creator())
app = FastAPI()
app.include_router(router=router)