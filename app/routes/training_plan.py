from fastapi import APIRouter
from app.utils.plan_calculator import generate_training_plan

router = APIRouter()

@router.get("/")
async def get_training_plan(weight: float, height: float, experience: str, focus: str | None = None, days_per_week: int = 3):
    plan = generate_training_plan(weight, height, experience, focus, days_per_week)
    return {"plan": plan}
