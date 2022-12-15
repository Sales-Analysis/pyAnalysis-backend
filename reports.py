from fastapi import APIRouter, UploadFile, status
from fastapi.responses import FileResponse, Response
from code_errors import InvalidFormatFile
from config import GlobalSettings, create_temp_dir
from validators import check_format_files

router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


@router.post("/uploadfile")
async def create_upload_file(file: UploadFile) -> Response:
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
