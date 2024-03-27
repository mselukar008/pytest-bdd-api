import os
import sys
import platform
from configparser import ConfigParser
from enum import Enum
from helpers.resources import root_folder

current_os = platform.system()

config = ConfigParser(comment_prefixes='/', allow_no_value=True)
if current_os == "Linux":
    config.read('config.ini')
else:
    config.read(os.path.join(root_folder, "config.ini"))


class SystemProperties(Enum):
    API_BASE_URL = ('base_url_countries', '')
    API_VERSION = ('api_version', '')
    API_URL = (f"{API_BASE_URL}/{API_VERSION}", '')
    GET_CURRENCY_API_URL = ('/currency/{}', '')

    def __init__(self, property_name, default_value):
        self.property_name = property_name
        self.default_value = default_value

    def raw_value(self):
        try:
            return sys._xoptions[self.property_name]
        except KeyError:
            # check in config file
            return config['SystemProperties'].get(self.property_name, None)

    def value(self):
        rv = self.raw_value()
        return self.default_value if rv is None else rv

    def bool_value(self) -> bool:
        rv = self.raw_value()
        if rv and 'true' == rv:
            return True
        if rv and 'false' == rv:
            return False
        return bool(self.default_value)
