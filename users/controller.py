from fastapi import APIRouter, Depends
from auth import model
from utils import util
from configs.connection import database

router = APIRouter()

@router.get("/users/me", response_model=model.UserList)
async def read_user_me(currentUser: model.UserList = Depends(util.get_current_active_user)):
    return currentUser

@router.get("/users")
async def find_all_user(
    currentUser: model.UserList = Depends(util.get_current_active_user)
):
    query = "select * from users"
    return await database.fetch_all(query=query, values={})
