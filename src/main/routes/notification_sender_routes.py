from fastapi import APIRouter

from src.main.factories.notification_sender_controller import (
    make_notification_sender_controller,
)
from src.main.routes.dtos import InputDTO
from src.presentation.controllers.notification_sender.notification_sender import (
    NotificationSenderController,
    SendNotificationInputPort,
)

router = APIRouter(prefix="/notification", tags=["Notification"])


def setup_routes(base_router: APIRouter):
    base_router.include_router(router)


class SendNotificationInputDTO(InputDTO, SendNotificationInputPort):
    pass


@router.post("/")
async def send_notification(
    request: SendNotificationInputDTO,
) -> None:
    controller: NotificationSenderController = make_notification_sender_controller()
    return await controller.handle(request)
