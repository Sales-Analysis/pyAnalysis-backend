from typing import List, Dict, Union
from fastapi import APIRouter
from fastapi.responses import FileResponse
from config import GlobalSettings
from models import AnalysisModel
from logger import logger


router = APIRouter()


@router.get("/report")
async def get_report() -> FileResponse:
    logger.info("get report")
    return FileResponse(path=f'{GlobalSettings.Config.BASEDIR}/data/abc_result.xlsx')


ANALYSIS_LIST: List[Dict[str, Union[str, bool]]] = [
    {
        'name': 'ABC',
        'description': 'Разделение товаров на три категории по степени их значимости. Поможет определить рентабельные '
                       'продукты, важных клиентов и поставщиков.',
        'status': True,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/abc.png'
    },
    {
        'name': 'XYZ',
        'description': 'Определение стабильности или устойчивости спроса на товары. Поможет определить какие товары '
                       'обязательно должны быть на складе или прилавке.',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/XYZ.png'
    },
    {
        'name': 'ABC XYZ',
        'description': 'Комбинация анализов которая поможет спланировать закупки. Результатом будет 6 групп которые '
                       'покажут самые прибыльные и востребованные товары.',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/ABC-XYZ.png'
    },
    {
        'name': 'FMR',
        'description': 'Анализ выявит насколько товары востребованы. Поможет определить оптимальное место хранения '
                       'товаров, снизить риск возникновения просроченности, и убрать из ассортимента непопулярную '
                       'продукцию.',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/FMR.png'
    },
    {
        'name': 'RFM',
        'description': 'Разделение клиентов по частоте и сумме покупок. Поможет выявить тех, кто больше и чаще платит '
                       'деньги, а кто давно ничего не покупал.',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/RFM.png'
    },
    {
        'name': 'FMR RFM',
        'description': 'some description',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/FMR-RFM.png'
    },
    {
        'name': 'VEN',
        'description': 'Разделение товаров или ресурсов по степени их важности или необходимости. Поможет определить '
                       'самые важные запчасти необходимые для производства или  приоритетные лекарственные',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/VEN.png'
    },
    {
        'name': 'SWOT',
        'description': 'some description',
        'status': False,
        'img': f'{GlobalSettings.Config.BASEDIR}./data/pictures/SWOT.png'
    },

]


@router.get("/typeAnalysis", response_model=List[AnalysisModel])
async def get_type_analysis():
    logger.info('get all type analysis')
    result = [AnalysisModel(**i) for i in ANALYSIS_LIST]
    logger.info('types of analysis successfully received')
    return result
