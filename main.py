import uvicorn
from config import get_config
from fastapi import FastAPI

settings = get_config()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.IP, port=settings.PORT, log_level="debug")
