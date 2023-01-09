import pytest


@pytest.fixture
def data_result():
    return {
        'код идентификатор PLU': [1, 2, 4, 3, 5],
        'наименование анализируемых позиций': [
            'Товар 1',
            'Товар 2',
            'Товар 4',
            'Товар 3',
            'Товар 5'],
        'данные по анализируемому критерию (продажи/оборот/прибыль)': [
            100, 50, 20, 8, 5
        ],
        'Доля': [54.64, 27.32, 10.93, 4.37, 2.73],
        'Аккум.доля': [54.64, 81.97, 92.9, 97.27, 100.0],
        'Категория': ['A', 'B', 'B', 'C', 'C'],
    }


@pytest.fixture
def data_input():
    return {
        'код идентификатор PLU': [1, 2, 3, 4, 5],
        'наименование анализируемых позиций': [
            'Товар 1',
            'Товар 2',
            'Товар 3',
            'Товар 4',
            'Товар 5'],
        'данные по анализируемому критерию (продажи/оборот/прибыль)': [
            100, 50, 8, 20, 5
        ],
    }


@pytest.fixture
def data_input_csv():
    return {'код идентификатор PLU': ['1', '2', '3', '4', '5'],
            'наименование анализируемых позиций': [
                'Товар 1',
                'Товар 2',
                'Товар 3',
                'Товар 4',
                'Товар 5'],
            'данные по анализируемому критерию (продажи/оборот/прибыль)': [
                '100', '50', '8', '20', '5']
            }


@pytest.fixture
def data_duplicate_value():
    return {
        'код идентификатор PLU': [1, 2, 2, 2, 3, 4, 5, 5, 5],
        'наименование анализируемых позиций': [
            'Товар 1',
            'Товар 2',
            'Товар 2',
            'Товар 2',
            'Товар 3',
            'Товар 4',
            'Товар 5',
            'Товар 5',
            'Товар 5',
        ],
        'данные по анализируемому критерию (продажи/оборот/прибыль)': [
            100, 50, 50, 50, 8, 20, 5, 5, 5
        ],
    }


@pytest.fixture
def data_duplicates():
    return [{'number_row': 4,
             'код идентификатор PLU': 2,
             'наименование анализируемых позиций': 'Товар 2',
             'данные по анализируемому критерию (продажи/оборот/прибыль)': 50
             },
            {'number_row': 5,
             'код идентификатор PLU': 2,
             'наименование анализируемых позиций': 'Товар 2',
             'данные по анализируемому критерию (продажи/оборот/прибыль)': 50
             },
            {'number_row': 9,
             'код идентификатор PLU': 5,
             'наименование анализируемых позиций': 'Товар 5',
             'данные по анализируемому критерию (продажи/оборот/прибыль)': 5
             },
            {'number_row': 10,
             'код идентификатор PLU': 5,
             'наименование анализируемых позиций': 'Товар 5',
             'данные по анализируемому критерию (продажи/оборот/прибыль)': 5
             }
            ]


@pytest.fixture
def data_output():
    return [('код идентификатор PLU',
             'наименование анализируемых позиций',
             'данные по анализируемому критерию (продажи/оборот/прибыль)',
             'Доля',
             'Аккум.доля',
             'Категория'
             ),
            (1, 'Товар 1', 100, '54.64', '54.64', 'A'),
            (2, 'Товар 2', 50, '27.32', '81.97', 'B'),
            ('4', 'Товар 4', 20, '10.93', '92.9', 'B'),
            ('3', 'Товар 3', 8, '4.37', '97.27', 'C'),
            ('5', 'Товар 5', 5, '2.73', '100.00', 'C')
            ]


@pytest.fixture
def analysis_list():
    return [
    {
        'name': 'ABC',
        'description': 'Разделение товаров на три категории по степени их значимости. Поможет определить рентабельные '
                       'продукты, важных клиентов и поставщиков.',
        'status': True
    },
    {
        'name': 'XYZ',
        'description': 'Определение стабильности или устойчивости спроса на товары. Поможет определить какие товары '
                       'обязательно должны быть на складе или прилавке.',
        'status': False},
    {
        'name': 'ABC XYZ',
        'description': 'Комбинация анализов которая поможет спланировать закупки. Результатом будет 6 групп которые '
                       'покажут самые прибыльные и востребованные товары.',
        'status': False
    },
    {
        'name': 'FMR',
        'description': 'Анализ выявит насколько товары востребованы. Поможет определить оптимальное место хранения '
                       'товаров, снизить риск возникновения просроченности, и убрать из ассортимента непопулярную '
                       'продукцию.',
        'status': False
    },
    {
        'name': 'RFM',
        'description': 'Разделение клиентов по частоте и сумме покупок. Поможет выявить тех, кто больше и чаще платит '
                       'деньги, а кто давно ничего не покупал.',
        'status': False
    },
    {'name': 'FMR RFM', 'description': 'some description', 'status': False},
    {
        'name': 'VEN',
        'description': 'Разделение товаров или ресурсов по степени их важности или необходимости. Поможет определить '
                       'самые важные запчасти необходимые для производства или  приоритетные лекарственные',
        'status': False
    },
    {'name': 'SWOT', 'description': 'some description', 'status': False},

]
