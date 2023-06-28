from fastapi import APIRouter
from models.users import User
from database.user import create_user,get_user, get_users, delete_users, update_users

router_user = APIRouter();


@router_user.post("/create", response_model=User)
def create(user: User):
    return create_user(user)

@router_user.get("/get/{id}")
def get_by_id(id:str):
    return  get_user(id)

@router_user.get("/all")
def get_all():
    return get_users()

@router_user.post("/delete")
def delete(user: User):
    return delete_users(user.dict())

@router_user.post("/updete")
def update(user: User):
    return update_users(user.dict())