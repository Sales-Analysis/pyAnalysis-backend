from typing import List, Dict, Union
from config import GlobalSettings
from utils.utils import create_name_project, create_temp_dir


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


def get_analysis_list() -> List[Dict[str, Union[str, bool]]]:
    return ANALYSIS_LIST


def upload_data_in_repository(upload_file: bytes, filename: str) -> None:
    temp_name_dir = create_name_project()
    path_temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/{temp_name_dir}'
    create_temp_dir(path=path_temp_dir)
    with open(
            f'{path_temp_dir}/{filename}',
            'wb'
    ) as f:
        f.write(upload_file)
