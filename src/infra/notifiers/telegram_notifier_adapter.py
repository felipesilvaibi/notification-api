from telegram import Bot

from src.domain.usecases.interfaces.telegram_notifier_adapter import (
    ITelegramNotifierAdapter,
)
from src.main.config.settings import settings
from src.presentation.errors.generic_errors import GenericServerError


class TelegramNotifierAdapter(ITelegramNotifierAdapter):
    async def send(self, recipient_id: str, message_content: str):
        bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

        try:
            await bot.send_message(
                chat_id=recipient_id, text=message_content, parse_mode="HTML"
            )
        except Exception as e:
            raise GenericServerError(
                f"Error on sending Telegram message to recipient {recipient_id}", e
            )
