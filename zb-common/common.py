import os
import configparser

class Util:

    def __init__(cfg_path):
        self.conf = configparser.ConfigParser()
        self.conf = conf.read(cfg_path)

    def get_env_value(self, key, section):
        return os.getenv("{}_{}".format(section, key), self.conf.get(section, key))
