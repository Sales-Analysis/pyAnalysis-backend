import uvicorn
import os
from config import get_config
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, FileResponse


settings = get_config()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/analysis/{type_analysis}")
async def get_analysis(type_analysis: str) -> JSONResponse:
    if type_analysis != 'ABC':
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': 'analysis not found'}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'hello world'},
    )


@app.get("/report")
async def get_report() -> FileResponse:
    basedir = os.path.abspath(os.path.dirname(__file__))
    return FileResponse(path=f'{basedir}/data/abc_result.xlsx')


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.get("IP"),
        port=int(settings.get("PORT")),
        log_level="debug"
    )
