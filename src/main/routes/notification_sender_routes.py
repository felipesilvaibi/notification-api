from fastapi import APIRouter

from main.factories.notification_sender import \
    make_notification_sender_controller
from presentation.controllers.notification_sender.notification_sender import (
    NotificationSenderController, SendNotificationInputPort,
    SendNotificationOutputPort)

router = APIRouter(prefix="/notification", tags=["Notification"])


def setup_routes(base_router: APIRouter):
    base_router.include_router(router)


class SendNotificationInputDTO(SendNotificationInputPort):
    pass


class SendNotificationOutputDTO(SendNotificationOutputPort):
    pass


@router.post("/", response_model=SendNotificationOutputDTO)
async def send_notification(
    request: SendNotificationInputDTO,
) -> SendNotificationOutputDTO:
    controller: NotificationSenderController = make_notification_sender_controller()
    return await controller.handle(request)
