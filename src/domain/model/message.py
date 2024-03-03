from datetime import datetime
from enum import Enum
from typing import Dict, Union

from pydantic import BaseModel


class Message(BaseModel):
    class MessageType(str, Enum):
        GENERIC = "GENERIC"
        TRADE = "TRADE"

    class GenericMessage(BaseModel):
        content: str

    class TradeMessage(BaseModel):
        class TradeAction(str, Enum):
            BUY = "BUY"
            SELL = "SELL"
            HOLD = "HOLD"

        trade_action: TradeAction
        indicators: Dict[str, Union[str, int, float, bool, datetime]]

    recipient_id: str
    type: MessageType
    message: Union[GenericMessage, TradeMessage]

    def format_message(self) -> str:
        if self.type == self.MessageType.GENERIC:
            return f"<p>{self.message.content}</p>"
        elif self.type == self.MessageType.TRADE:
            indicators_str = "\n".join(
                f"• <b>{key}</b>: {value}"
                for key, value in self.message.indicators.items()
            )
            action_emoji = {
                "BUY": "🟢",
                "HOLD": "🟡",
                "SELL": "🔴",
            }.get(self.message.trade_action)

            return (
                f"<b>🚨 Trade action</b>: {action_emoji} <b>{self.message.trade_action}</b>\n\n"
                f"<b>Indicators</b>:\n{indicators_str}"
            )
