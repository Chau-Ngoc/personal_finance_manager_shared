from abc import ABC, abstractmethod
from typing import Awaitable, Callable, Optional

from personal_finance_manager_shared.events.exchange_infos import ExchangeInfo


class BaseListener(ABC):
    exchange_info: ExchangeInfo
    __connection: Optional["AbstractRobustConnection"]  # noqa: F821
    __channel: Optional["AbstractChannel"]  # noqa: F821

    @classmethod
    @abstractmethod
    async def connect(cls, channel_number: int | None, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def disconnect(cls):
        raise NotImplementedError

    @abstractmethod
    async def listen(self, callback: Callable[["AbstractIncomingMessage"], Awaitable[None]], **kwargs):  # noqa: F821
        raise NotImplementedError

    @property
    @abstractmethod
    def connection(self):
        raise NotImplementedError
