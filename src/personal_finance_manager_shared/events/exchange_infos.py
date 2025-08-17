from typing import NamedTuple


class ExchangeInfo(NamedTuple):
    type: str
    name: str
    topic: str


NewExpenseNotificationsExchangeInfo = ExchangeInfo(
    type="topic", name="notifications", topic="new_expense.notifications"
)
