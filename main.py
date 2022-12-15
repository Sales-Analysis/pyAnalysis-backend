import uvicorn
import reports
from code_errors import InvalidFormatFile
from config import get_config
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


settings = get_config()

app = FastAPI()


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


app.include_router(reports.router)


@app.exception_handler(InvalidFormatFile)
async def invalid_format_file(request: Request, exc: InvalidFormatFile) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": f"Неверный формат файла {exc.name}. Допустимые форматы (xlsx, csv)."}
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.get("IP"),
        port=int(settings.get("PORT")),
        log_level="debug"
    )
