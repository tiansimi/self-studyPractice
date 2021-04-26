import configparser
import os
from interface_automation.tools import project_path


class Read_config:
    def get_config(self, section, option):
        cf = configparser.ConfigParser()
        path = os.path.join(project_path.path, 'conf', 'case.ini')
        cf.read(path)
        return cf[section][option]


print(Read_config().get_config('DB', 'db_config'))
