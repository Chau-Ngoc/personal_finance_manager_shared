from abc import ABC, abstractmethod
from typing import Optional

from personal_finance_manager_shared.events.exchange_infos import ExchangeInfo


class BasePublisher(ABC):
    exchange_info: ExchangeInfo
    __connection: Optional["AbstractRobustConnection"]  # noqa: F821

    @classmethod
    @abstractmethod
    async def connect(cls, channel_number: int | None = None, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def disconnect(cls):
        raise NotImplementedError

    @abstractmethod
    async def publish(self, message: bytes):
        raise NotImplementedError

    @property
    @abstractmethod
    def connection(self) -> "AbstractRobustConnection":  # noqa: F821
        raise NotImplementedError
