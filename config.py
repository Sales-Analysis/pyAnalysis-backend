import os
import shutil
import tempfile
import pathlib
import uuid
from pydantic import BaseSettings
from dotenv import dotenv_values


class GlobalSettings(BaseSettings):
    class Config:
        env_file: str = ".env"
        BASEDIR: str = os.path.abspath(os.path.dirname(__file__))


dotenv_values = dotenv_values(GlobalSettings.Config.env_file)


def get_config():
    return dotenv_values


def create_temp_dir():
    myuuid = str(uuid.uuid4())
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/{myuuid}'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
        return temp_dir


def del_temp_dir():
    temp_dir = f'{GlobalSettings.Config.BASEDIR}/data/temp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
