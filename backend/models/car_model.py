from pydantic import BaseModel
from typing import Optional


class CarData(BaseModel):
    brand: str
    fuel: str
    gearbox: str
    year: int
    mileage_kms: int

    class Config:
        allow_population_by_field_name = True

        schema_extra = {
            "example": {
                "brand": "SEAT",
                "year": 2016,
                "fuel": "Gasolina",
                "gearbox": "Manual",
                # "location": "Viladecans",
                "mileage_kms": 67000,
            }
        }


class Car(BaseModel):
    brand: str
    year: Optional[int]
    fuel: str
    gearbox: str
    location: Optional[str]
    mileage: Optional[int]

    class Config:
        allow_population_by_field_name = True

        schema_extra = {
            "example": {
                "brand": "BMW",
                "year": 2018,
                "fuel": "Gasolina",
                "gearbox": "Automatica",
                "location": "Viladecans",
                "mileage": 10000,
            }
        }
