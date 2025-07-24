import logging

from personal_finance_manager_shared.loggers.base_logger import BaseLogger


class ConsoleLogger(BaseLogger):
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        ch = logging.StreamHandler()
        ch.setLevel(level)

        formatter = logging.Formatter("{asctime} {levelname} {name} {message}", style="{")
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def debug(self, msg: str, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def exception(self, msg: str, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)
