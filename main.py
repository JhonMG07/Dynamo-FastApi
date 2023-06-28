from fastapi import FastAPI
from database.db import create_tables
from routes.users import router_user
app = FastAPI();

app.include_router(router_user,prefix="/user")

create_tables()