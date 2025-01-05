import sys
from loguru import logger as loguru_logger

from app.config import DEBUG


class Logging:
    def __init__(self):
        self.level = "DEBUG" if DEBUG else "DEBUG"

    def setup_logger(self):
        loguru_logger.remove()
        loguru_logger.add(sys.stdout, level=self.level)
        loguru_logger.add("./logs/file_{time}.log", level=self.level, rotation="00:00")

        return loguru_logger


logging = Logging()
logger = logging.setup_logger()
