import yaml
from pathlib import Path
from typing import Any, Optional, Dict
import logging

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class YamlReader:
    """
    A utility class for reading and accessing data from YAML files.
    """

    def __init__(self, filepath: Path):
        """
        Initializes the YamlReader instance.

        :param filepath: The path to the YAML file to be read.
        """
        self.filepath: Path = filepath
        self.data: Optional[Dict[str, Any]] = None

    def load(self) -> Optional[Dict[str, Any]]:
        """
        Loads YAML data from the file into memory.

        :return: A dictionary containing the YAML data, or None if an error occurs.
        """
        try:
            logger.info("reading YAML file...")
            with open(self.filepath, 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)
                logger.info(f"YAML file loaded successfully: {self.filepath}")
            return self.data
        except FileNotFoundError:
            logger.error(f"File not found: {self.filepath}")
        except yaml.YAMLError as e:
            logger.error(f"YAML parsing error: {e}")
        return None
