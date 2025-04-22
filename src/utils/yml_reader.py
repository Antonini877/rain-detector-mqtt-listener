import yaml
from pathlib import Path

class YamlReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        """Loads YAML data from the file into memory."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)
            return self.data
        except FileNotFoundError:
            print(f"File not found: {self.filepath}")
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")
        return None

    def get(self, key, default=None):
        """Retrieves a value by key from the loaded data."""
        if self.data is None:
            self.load()
        return self.data.get(key, default) if self.data else default
