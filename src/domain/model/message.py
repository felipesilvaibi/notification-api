from enum import Enum
from typing import Optional, Union

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

        class Indicators(BaseModel):
            weekly_rsi: Optional[int] = None
            monthly_rsi: Optional[int] = None
            mvrv_z_score: Optional[int] = None

        trade_action: TradeAction
        indicators: Indicators

    recipient_id: str
    type: MessageType
    message: Union[GenericMessage, TradeMessage]

    # def __init__(self, **data):
    #     super().__init__(**data)
    #     if self.type == self.MessageType.GENERIC:
    #         self.message = self.GenericMessage(**self.message.model_dump())
    #     elif self.type == self.MessageType.TRADE:
    #         self.message = self.TradeMessage(**self.message.model_dump())

    def format_message(self) -> str:
        if self.type == self.MessageType.GENERIC:
            return self.message.content
        elif self.type == self.MessageType.TRADE:
            return (
                f"Trade action: {self.message.trade_action}\n"
                f"Weekly RSI: {self.message.indicators.weekly_rsi}\n"
                f"Monthly RSI: {self.message.indicators.monthly_rsi}\n"
                f"MVRV Z-Score: {self.message.indicators.mvrv_z_score}"
            )
        return ""
