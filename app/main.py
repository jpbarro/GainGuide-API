from fastapi import FastAPI
from .routes import user_data, training_plan

app = FastAPI(title="GainGuide API")

# Include routes
app.include_router(user_data.router, prefix="/user", tags=["User Data"])
app.include_router(training_plan.router, prefix="/plan", tags=["Training Plan"])

@app.get("/")
async def root():
    return {"message": "Welcome to the GainGuide API"}
