class NotFoundAnalysisError(Exception):
    """Not found analysis."""


class FileIsEmptyError(Exception):
    """File is empty."""


class HeaderNotFoundError(Exception):
    """File is not header"""


class InvalidFormatFile(Exception):
    """Format file is not valid."""
    def __init__(self, name: str):
        self.name = name
