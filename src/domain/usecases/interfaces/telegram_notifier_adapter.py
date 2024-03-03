from abc import ABC, abstractmethod


class ITelegramNotifierAdapter(ABC):

    @abstractmethod
    def send(self, recipient_id: str, message_content: str) -> None:
        pass
