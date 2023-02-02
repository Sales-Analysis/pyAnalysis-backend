from fastapi import APIRouter, UploadFile, status, File, Depends
from fastapi.responses import Response, JSONResponse
from services.reports import upload_data_in_repository
from models.models import AnalysisModel2
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
    upload_data_in_repository(file=file)
    logger.info("File successfully uploaded")
    return Response(content="File successfully uploaded", status_code=status.HTTP_200_OK)
