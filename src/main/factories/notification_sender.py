from src.domain.usecases.telegram_notifier import TelegramNotifierUsecase
from src.infra.notifiers.telegram_notifier_adapter import TelegramNotifierAdapter
from src.presentation.controllers.notification_sender.notification_sender import (
    NotificationSenderController,
)


def make_notification_sender_controller() -> NotificationSenderController:
    telegram_notifier_adapter = TelegramNotifierAdapter()
    telegram_notifier_usecase = TelegramNotifierUsecase(telegram_notifier_adapter)

    return NotificationSenderController(telegram_notifier_usecase)
