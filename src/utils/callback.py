import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def handle_message(topic, payload):
    logger.info(f"Received message: {payload} on topic: {topic}")