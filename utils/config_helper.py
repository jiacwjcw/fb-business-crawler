import os

from utils.file_utils import *


class ConfigHelper:

    def __init__(self):
        self.config = self._read_config()

    @staticmethod
    def _read_config():
        config_path = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config.yaml'
        return read_yaml_file(config_path)

    def get_fb_account(self):
        return self.config["fb_acc"]

    def get_fb_password(self):
        return self.config["fb_pwd"]

    def get_revenue_host(self):
        return self.config["revenue_host"]

    def get_posts_analysis_host(self):
        return self.config["posts_analysis_host"]
