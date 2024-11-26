from pydantic import BaseModel

class UserData(BaseModel):
    weight: float
    height: float
    experience: str  # beginner, intermediate, advanced
    focus: str | None = None  # Optional: muscle group focus
    days_per_week: int
