from src.domain.usecases.telegram_notifier import TelegramNotifierUsecase
from src.infra.notifiers.telegram_notifier_adapter import TelegramNotifierAdapter


def make_telegram_notifier_usecase() -> TelegramNotifierUsecase:
    telegram_notifier_adapter = TelegramNotifierAdapter()
    return TelegramNotifierUsecase(telegram_notifier_adapter)
