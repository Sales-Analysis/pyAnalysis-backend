import uvicorn
from config import get_config
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse


settings = get_config()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/analysis/{type_analysis}")
def get_analysis(type_analysis):
    if type_analysis == 'ABC':
        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'message': 'hello world'}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': 'analysis not found'}
        )


if __name__ == "__main__":
    uvicorn.run(app, host=settings.get("IP"), port=int(settings.get("PORT")), log_level="debug")
