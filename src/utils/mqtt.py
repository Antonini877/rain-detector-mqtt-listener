import paho.mqtt.client as mqtt
import logging
from typing import Callable, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class MQTTClient:
    """
    A wrapper class for the Paho MQTT client to simplify MQTT operations.
    """

    def __init__(self, broker: str, port: int, client_id: str, username: Optional[str] = None, password: Optional[str] = None):
        """
        Initializes the MQTTClient.

        :param broker: The MQTT broker address.
        :param port: The port to connect to the MQTT broker.
        :param client_id: The client ID to use for the MQTT connection.
        :param username: Optional username for authentication.
        :param password: Optional password for authentication.
        """
        self.broker = broker
        self.port = int(port)
        self.client_id = client_id
        self.username = username
        self.password = password
        self.client = mqtt.Client(client_id)

        if username and password:
            self.client.username_pw_set(username, password)

    def connect(self) -> None:
        """
        Connects to the MQTT broker and sets up the on_connect callback.
        """
        def on_connect(client: mqtt.Client, userdata: dict, flags: dict, rc: int) -> None:
            """
            Callback for when the client connects to the broker.

            :param client: The MQTT client instance.
            :param userdata: User-defined data of any type.
            :param flags: Response flags sent by the broker.
            :param rc: The connection result.
            """
            if rc == 0:
                logger.info("Connected to MQTT Broker!")
            else:
                logger.warning(f"Failed to connect, return code {rc}")
        self.client.on_connect = on_connect
        self.client.tls_set()
        self.client.connect(self.broker, self.port)

    def publish(self, topic: str, payload: str) -> None:
        """
        Publishes a message to a specific topic.

        :param topic: The topic to publish the message to.
        :param payload: The message payload to send.
        """
        result = self.client.publish(topic, payload)
        status = result[0]
        if status == 0:
            logging.info(f"Message sent to topic {topic}")
        else:
            logging.info(f"Failed to send message to topic {topic}")

    def subscribe(self, topic: str, callback: Callable[[str, str], None]) -> None:
        """
        Subscribes to a specific topic and sets up a callback for incoming messages.

        :param topic: The topic to subscribe to.
        :param callback: A function to handle incoming messages. It should accept two arguments: topic and payload.
        """
        def on_message(client: mqtt.Client, userdata: dict, msg: mqtt.MQTTMessage) -> None:
            """
            Callback for when a message is received.

            :param client: The MQTT client instance.
            :param userdata: User-defined data of any type.
            :param msg: The MQTT message received.
            """
            callback(msg.topic, msg.payload.decode())
        self.client.subscribe(topic)
        self.client.on_message = on_message

    def loop_forever(self) -> None:
        """
        Starts the MQTT client loop to process network traffic and dispatch callbacks.
        """
        logging.info("Starting MQTT loop...")
        self.client.loop_forever()