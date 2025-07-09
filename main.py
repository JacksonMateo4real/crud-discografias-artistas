from fastapi import FastAPI
from app.routes import manager




app = FastAPI()


app.include_router(manager)

