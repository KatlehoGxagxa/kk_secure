import json, logging
from fastapi import Depends, FastAPI



app = FastAPI()

from app.quadratic_equation.route import route
app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "Quadratic Equation"}