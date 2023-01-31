from typing import List
from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import GlobalSettings
from models import AnalysisModel
from logger import logger
from services.reports import get_analysis_list

router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    logger.info("get report")
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


@router.get("/typeAnalysis", response_model=List[AnalysisModel])
async def get_type_analysis():
    logger.info('get all type analysis')
    result = [AnalysisModel(**i) for i in get_analysis_list()]
    logger.info('types of analysis successfully received')
    return result
