from fastapi import APIRouter
from pydantic import BaseModel
from ..schemas import UserData

router = APIRouter()

@router.post("/")
async def save_user_data(data: UserData):
    # Mock saving the data (could save to a DB later)
    return {"message": "User data saved successfully", "data": data}
