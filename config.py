class GlobalSettings:
    IP: str = "127.0.0.1"
    PORT: int = 9090


def get_config():
    return GlobalSettings()
