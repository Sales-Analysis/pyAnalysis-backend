import uvicorn
from config import GlobalSettings
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run(app, host=GlobalSettings.IP, port=GlobalSettings.PORT, log_level="debug")
