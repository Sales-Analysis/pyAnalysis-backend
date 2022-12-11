#TODO download xlsx and csv
from typing import List

CONTENT_TYPE: List[str] = [
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-excel",
    "text/csv",
]


def check_format_files(content_type: str) -> bool:
    if content_type in CONTENT_TYPE:
        return True
