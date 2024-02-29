from datetime import datetime

from pydantic import BaseModel

from presentation.errors.generic_errors import GenericServerError


class SendNotificationInputPort(BaseModel):
    param_id_example: str


class SendNotificationOutputPort(BaseModel):
    date_of_transaction: datetime


class NotificationSenderController:

    async def handle(
        self, input_port: SendNotificationInputPort
    ) -> SendNotificationOutputPort:
        return SendNotificationOutputPort(date_of_transaction=datetime.now())
