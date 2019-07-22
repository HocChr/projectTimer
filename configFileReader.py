import re
import os


class ConfigFileReader:
    def __init__(self):
        path = os.getcwd()
        self.file_path = path + '\config.txt'

    def getValue(self, key):
        with open(self.file_path, 'r') as configFile:
            for line in configFile:
                line = line.replace(' ', '')
                head, sep, tail = line.partition('#')
                res = re.split(':', head)
                if len(res) > 1 and key in res:
                    return res[1]

        return ''







