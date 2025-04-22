import requests
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class TelegramBot:
    """
    A class to interact with the Telegram Bot API for sending messages.
    """

    def __init__(self, base_url: str, token: str, chat_id: str):
        """
        Initializes the TelegramBot instance.

        :param base_url: The base URL for the Telegram Bot API.
        :param token: The token for the Telegram bot.
        :param chat_id: The chat ID where messages will be sent.
        """
        self.chat_id = chat_id
        self.url = base_url.format(token=token)

    def send_message(self, text: str) -> Optional[dict]:
        """
        Sends a text message to a Telegram chat using the bot API.

        :param text: The text of the message to be sent.
        :return: The response from the Telegram API as a dictionary, or None if an error occurs.
        """
        payload = {
            'chat_id': self.chat_id,
            'text': text
        }

        try:
            response = requests.post(self.url, data=payload)
            response.raise_for_status()  # Raises an error if the HTTP response is an error
            logger.info(f"Message sent to Telegram: {text}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending message: {e}")
            return None