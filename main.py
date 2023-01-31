import uvicorn
import upload_file
from api import reports
from code_errors import InvalidFormatFile
from config import get_config
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from logger import logger

settings = get_config()

app = FastAPI()


app.include_router(reports.router)
app.include_router(upload_file.router)


@app.exception_handler(InvalidFormatFile)  # for func post_report in upload_file.py
async def invalid_format_file(request: Request, exc: InvalidFormatFile) -> JSONResponse:
    logger.error(f'invalid file format {exc.name}. Acceptable format (xlsx, csv).')
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

