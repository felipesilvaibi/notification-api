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
            return self.message.content
        elif self.type == self.MessageType.TRADE:
            indicators_str = "\n".join(
                f"• **{key}**: {value}"
                for key, value in self.message.indicators.items()
            )
            return (
                f"*Trade action*: **{self.message.trade_action}**\n\n"
                f"*Indicators*:\n{indicators_str}"
            )
