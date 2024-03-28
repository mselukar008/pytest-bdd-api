import configparser
from helpers import utils
from helpers.logger import Logger

logger = Logger().getLogger()

parser = configparser.ConfigParser()
confFilePath = utils.get_abs_dir(r'/config.ini')
parser.read(confFilePath)

global API_BASE_URL
global API_VERSION
global CURRENCY_URL
global API_URL_WITH_VERSION


def load_config_variables():
    global API_BASE_URL
    global API_VERSION
    global CURRENCY_URL
    global API_URL_WITH_VERSION

    API_BASE_URL = parser.get("SystemProperties", 'base_url_countries')
    API_VERSION = parser.get("SystemProperties", 'api_version')
    CURRENCY_URL = parser.get("SystemProperties", 'currency_api')
    API_URL_WITH_VERSION = f"{API_BASE_URL}/{API_VERSION}"
