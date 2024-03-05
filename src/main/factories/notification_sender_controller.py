from src.main.factories.telegram_notifier_usecase import make_telegram_notifier_usecase
from src.presentation.controllers.notification_sender.notification_sender import (
    NotificationSenderController,
)


def make_notification_sender_controller() -> NotificationSenderController:
    telegram_notifier_usecase = make_telegram_notifier_usecase()
    return NotificationSenderController(telegram_notifier_usecase)
