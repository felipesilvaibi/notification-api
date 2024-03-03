from typing import Union

from pydantic import BaseModel

from src.domain.model.message import Message
from src.domain.usecases.interfaces.telegram_notifier_adapter import (
    ITelegramNotifierAdapter,
)


class TelegramNotifierUsecaseInputPort(BaseModel):
    recipient_id: str
    message_type: Message.MessageType
    message: Union[Message.GenericMessage, Message.TradeMessage]


class TelegramNotifierUsecase:

    def __init__(self, telegram_notifier: ITelegramNotifierAdapter):
        self.telegram_notifier = telegram_notifier

    async def send(
        self, send_telegram_notification_input_port: TelegramNotifierUsecaseInputPort
    ):
        model_message = Message(
            recipient_id=send_telegram_notification_input_port.recipient_id,
            type=send_telegram_notification_input_port.message_type,
            message=send_telegram_notification_input_port.message,
        )

        await self.telegram_notifier.send(
            recipient_id=model_message.recipient_id,
            message_content=model_message.format_message(),
        )
