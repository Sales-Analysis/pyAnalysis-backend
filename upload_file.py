from fastapi import APIRouter, UploadFile, status, File, Depends
from fastapi.responses import Response, JSONResponse
from code_errors import InvalidFormatFile
from config import create_temp_dir, create_name_project, GlobalSettings
from models import AnalysisModel2
from validators import check_format_files
from logger import logger

router = APIRouter()


@router.post("/uploadreport")
async def post_report(prop: AnalysisModel2 = Depends(), file: UploadFile = File(...)) -> Response:
    logger.info("post request for upload report")
    if prop.type != 'ABC':
        logger.error("type analysis is not ABC")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'error': 'type analysis not found'}
        )
    upload_file = file.file.read()
    if not check_format_files(content_type=file.content_type):
        logger.error("Format file is not valid")
        raise InvalidFormatFile(name=file.filename)
    temp_name_dir = create_name_project()
    create_temp_dir(temp_name_dir)
    with open(
            f'{GlobalSettings.Config.BASEDIR}/data/{temp_name_dir}/{file.filename}',
            'wb'
    ) as f:
        f.write(upload_file)
    logger.info("File successfully uploaded")
    return Response(content="File successfully uploaded", status_code=status.HTTP_200_OK)
