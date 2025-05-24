from fastapi import APIRouter
from typing import List

from src.data.mock_generator import generate_mock_data
from src.models.mock_models import ChargerData

router = APIRouter()

@router.get("/chargers", response_model=List[ChargerData])
def get_chargers():
    return generate_mock_data()
