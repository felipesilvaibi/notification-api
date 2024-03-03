from enum import Enum
from typing import Union

from pydantic import BaseModel

from src.domain.model.message import Message
from src.domain.usecases.telegram_notifier import (
    TelegramNotifierUsecase,
    TelegramNotifierUsecaseInputPort,
)


class SendNotificationInputPort(BaseModel):
    class NotificationType(str, Enum):
        TELEGRAM = "TELEGRAM"

    type: NotificationType
    recipient_id: str
    message_type: Message.MessageType
    message: Union[Message.GenericMessage, Message.TradeMessage]


class NotificationSenderController:

    def __init__(self, send_telegram_notification_usecase: TelegramNotifierUsecase):
        self.telegram_notifier_usecase = send_telegram_notification_usecase

    async def handle(self, input_port: SendNotificationInputPort) -> None:
        if input_port.type == SendNotificationInputPort.NotificationType.TELEGRAM:
            telegram_notifier_usecase_input_port = TelegramNotifierUsecaseInputPort(
                recipient_id=input_port.recipient_id,
                message_type=input_port.message_type,
                message=input_port.message,
            )

            return await self.telegram_notifier_usecase.send(
                telegram_notifier_usecase_input_port
            )
        else:
            raise NotImplementedError("Notification type not implemented")
