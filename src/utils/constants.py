from utils.yml_reader import YamlReader

configs = YamlReader('config.yml').load()

class Constants:
    APP_CONFIGS = configs["app"]
    
    TELEGRAM_CONFIGS = APP_CONFIGS["telegram"]
    TELEGRAM_BASE_URL = TELEGRAM_CONFIGS["base_url"]
    TELEGRAM_MESSAGE = TELEGRAM_CONFIGS["message"]