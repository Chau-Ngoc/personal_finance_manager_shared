import logging
import time
from abc import ABC, abstractmethod

logging.Formatter.converter = time.gmtime


class BaseLogger(ABC):
    @abstractmethod
    def debug(self, msg: str, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def info(self, msg: str, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def warning(self, msg: str, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def error(self, msg: str, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def critical(self, msg: str, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def exception(self, msg: str, *args, **kwargs):
        raise NotImplementedError
