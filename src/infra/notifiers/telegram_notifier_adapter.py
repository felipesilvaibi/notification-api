from telegram import Bot

from src.domain.usecases.interfaces.telegram_notifier_adapter import (
    ITelegramNotifierAdapter,
)
from src.main.config.logger import logger
from src.main.config.settings import settings
from src.presentation.errors.generic_errors import GenericServerError


class TelegramNotifierAdapter(ITelegramNotifierAdapter):
    async def send(self, recipient_id: str, message_content: str):
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

        try:
            await bot.send_message(chat_id=recipient_id, text=message_content)
        except Exception as e:
            base_error_message = (
                f"Error on sending Telegram message to recipient {recipient_id}"
            )

            logger.error(f"{base_error_message}: {e}")
            raise GenericServerError(f"{base_error_message}")
