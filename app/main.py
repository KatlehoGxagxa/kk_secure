import json, logging
from fastapi import Depends, FastAPI
from app.db_models.main import session

print(session)
app = FastAPI()

# from app.feature.login import route
# app.include_router(route.router)

# from app.feature.get_details import route
# app.include_router(route.router)


@app.get("/")
async def root():
    return {"KK Secure Application"}

