import uvicorn
from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get("/")
def read():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
