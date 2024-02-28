from fastapi import APIRouter

from main.factories.notification_sender import make_notification_sender_controller
from main.routes.protocols import InputDTO, OutputDTO
from presentation.controllers.notification_sender.notification_sender import (
    NotificationSenderController,
    SendNotificationInputPort,
    SendNotificationOutputPort,
)

router = APIRouter(prefix="/notification", tags=["Notification"])


def setup_routes(base_router: APIRouter):
    base_router.include_router(router)


class SendNotificationInputDTO(InputDTO, SendNotificationInputPort):
    pass


class SendNotificationOutputDTO(OutputDTO, SendNotificationOutputPort):
    pass


@router.post("/", response_model=SendNotificationOutputDTO)
async def run_annual_readjustment_applied(
    request: SendNotificationInputDTO,
) -> SendNotificationOutputDTO:
    input_dto = SendNotificationInputDTO.model_validate(request["body"])

    controller: NotificationSenderController = make_notification_sender_controller(
        input_dto
    )
    return controller.handle(input_dto)
