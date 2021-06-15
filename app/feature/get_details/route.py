import json, logging
from fastapi import APIRouter, Depends

# Importing input_models, that will be used route paramaters
from app.db_models.models import organisationsModel
from app.db_models.models import accountsModel
from app.db_models.models import usersModel

# Import the service for the route
from app.feature.get_details.service import get_details

router = APIRouter()

@router.post("/quadratic_equation", tags=["equations"])
async def quadratic_equation(input_model: QuadraticEquationModel):
    return QuadraticEquation(inputs = input_model ).quadratic_equation()