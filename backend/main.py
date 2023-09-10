import uvicorn
from fastapi import FastAPI
from config import settings
from backend.routes import car_routes

app = FastAPI()


# Include the car_routes router
app.include_router(car_routes.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
