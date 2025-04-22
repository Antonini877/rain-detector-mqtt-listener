import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self, base_url, token, chat_id):
        self.chat_id = chat_id
        self.url = base_url.format(token=token)

       
    def send_message(self, text):
        """
        Sends a text message to Telegram using the bot API.
        :param text: The text of the message to be sent.
        """
        payload = {
            'chat_id': self.chat_id,
            'text': text
        }
        
        try:
            response = requests.post(self.url, data=payload)
            response.raise_for_status()  # Raises an error if the HTTP response is an error
            logger.info(f"Message sent to Telegram: {text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending message: {e}")


