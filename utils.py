import os
import shutil
import uuid


def create_name_project() -> str:
    return str(uuid.uuid4())


def create_temp_dir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def del_temp_dir(path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
