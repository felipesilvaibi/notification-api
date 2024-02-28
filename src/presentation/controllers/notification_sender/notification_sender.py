# Supondo que os erros, helpers e protocolos estejam definidos em módulos Python correspondentes
from datetime import datetime

from pydantic import BaseModel


class SendNotificationInputPort(BaseModel):
    param_id_example: str


class SendNotificationOutputPort(BaseModel):
    date_of_transaction: datetime


class NotificationSenderController:

    async def handle(
        self, input_port: SendNotificationInputPort
    ) -> SendNotificationOutputPort:
        print(input_port.param_id_example)
        return SendNotificationOutputPort(date_of_transaction=datetime.now())
