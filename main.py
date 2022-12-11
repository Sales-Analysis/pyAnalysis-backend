import uvicorn
import aiofiles

from code_errors import InvalidFormatFile
from config import get_config, GlobalSettings, create_temp_dir
from fastapi import FastAPI, status, File, UploadFile
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse, Response

from validators import check_format_files

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
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


@app.exception_handler(InvalidFormatFile)
def invalid_format_file(request: Request, exc: InvalidFormatFile) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": f"Неверный формат файла {exc.name}. Допустимые форматы (xlsx, csv)."}
    )


@app.post("/uploadfile")
def create_upload_file(file: UploadFile) -> Response:
    upload_file = file.file.read()
    if not check_format_files(content_type=file.content_type):
        raise InvalidFormatFile(name=file.filename)
    create_temp_dir()
    with open(
            f'{GlobalSettings.Config.BASEDIR}/data/temp/{file.filename}',
            'wb'
    ) as f:
        f.write(upload_file)
    return Response(content="File successfully uploaded", status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.get("IP"),
        port=int(settings.get("PORT")),
        log_level="debug"
    )

