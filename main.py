import uvicorn
from config import GlobalSettings
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run(app, host=GlobalSettings.ip, port=GlobalSettings.port, log_level="debug")
