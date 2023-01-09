from typing import List, Dict, Union

from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import GlobalSettings
from models import AnalysisModel

router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


ANALYSIS_LIST: List[Dict[str, Union[str, bool]]] = [
    {'name': 'ABC', 'description': 'some description', 'status': True},
    {'name': 'XYZ', 'description': 'some description', 'status': False},
    {'name': 'ABC XYZ', 'description': 'some description', 'status': False},
    {'name': 'FMR', 'description': 'some description', 'status': False},
    {'name': 'RFM', 'description': 'some description', 'status': False},
    {'name': 'FMR RFM', 'description': 'some description', 'status': False},
    {'name': 'VEN', 'description': 'some description', 'status': False},
    {'name': 'SWOT', 'description': 'some description', 'status': False},

]


@router.get("/typeAnalysis", response_model=List[AnalysisModel])
async def get_type_analysis():
    result = [AnalysisModel(**i) for i in ANALYSIS_LIST]
    return result
