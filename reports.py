from fastapi import APIRouter, UploadFile, status, File, Depends
from fastapi.responses import FileResponse, Response, JSONResponse
from pydantic.main import BaseModel

from code_errors import InvalidFormatFile
from config import GlobalSettings, create_temp_dir
from models import AnalysisModel2
from validators import check_format_files

router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


@router.post("/uploadreport")
async def post_report(prop: AnalysisModel2 = Depends(), file: UploadFile = File(...)) -> Response:
    if prop.type != 'ABC':
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': 'type analysis not found'}
        )
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
