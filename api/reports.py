from typing import List
from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import GlobalSettings
from models import AnalysisModel
from logger import logger
from services.services import get_analysis_list

router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    logger.info("get report")
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


@router.get("/typeAnalysis", response_model=List[AnalysisModel])
async def get_type_analysis():
    logger.info('get all type analysis')
    analysis_list = get_analysis_list()
    result = [AnalysisModel(**i) for i in analysis_list]
    logger.info('types of analysis successfully received')
    return result
