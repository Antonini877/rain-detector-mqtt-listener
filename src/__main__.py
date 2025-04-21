from utils.mqtt import MQTTClient
import logging
from dotenv import load_dotenv
from utils.callback import handle_message
import os

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    mqtt_client = MQTTClient(
        broker=os.getenv("MQTT_BROKER_URL"),
        port=os.getenv("MQTT_BROKER_PORT"),
        client_id=os.getenv("MQTT_BROKER_CLIENT_ID"),
        username=os.getenv("MQTT_BROKER_USERNAME"),
        password=os.getenv("MQTT_BROKER_PASSWORD")   
    )
    
    try:
        mqtt_client.connect()
        mqtt_client.subscribe(os.getenv("MQTT_BROKER_TOPIC"), handle_message)
        mqtt_client.loop_forever()
    except KeyboardInterrupt:
        logging.warning("Disconnecting from broker...")

if __name__ == "__main__":
    main()