import os
import shutil
import uuid
from config import GlobalSettings


def create_name_project() -> str:
    return str(uuid.uuid4())


def create_temp_dir(path: str) -> None:
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/{path}'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)


def del_temp_dir():
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
