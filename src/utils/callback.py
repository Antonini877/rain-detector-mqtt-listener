import logging
from dotenv import load_dotenv
import os
from services.telegram import TelegramBot
from utils.constants import Constants as c

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def handle_message(topic, payload):
    logger.info(f"Received message: {payload} on topic: {topic}")

    bot = TelegramBot(
        base_url=c.TELEGRAM_BASE_URL,
        token=os.getenv("TELEGRAM_APPLICATION_TOKEN"),
        chat_id=os.getenv("TELEGRAM_APPLICATION_CHAT_ID")   
    )
    bot.send_message(c.TELEGRAM_MESSAGE)

