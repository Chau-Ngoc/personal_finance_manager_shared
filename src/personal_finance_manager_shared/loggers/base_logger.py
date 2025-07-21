import logging
import time
from abc import ABC, abstractmethod

logging.Formatter.converter = time.gmtime


class BaseLogger(ABC):
    @abstractmethod
    def debug(self, msg: str, *args, **kwargs):
        pass

    @abstractmethod
    def info(self, msg: str, *args, **kwargs):
        pass

    @abstractmethod
    def warning(self, msg: str, *args, **kwargs):
        pass

    @abstractmethod
    def error(self, msg: str, *args, **kwargs):
        pass

    @abstractmethod
    def critical(self, msg: str, *args, **kwargs):
        pass

    @abstractmethod
    def exception(self, msg: str, *args, **kwargs):
        pass
