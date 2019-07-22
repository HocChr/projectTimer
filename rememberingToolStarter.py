from os import path
from configFileReader import ConfigFileReader
from random import randint
import time
import os
import subprocess

class RememberingToolStarter:
    def __init__(self):
        reader = ConfigFileReader()
        self._minTime = reader.getValue('RemberNotBefore')
        self._maxTime = reader.getValue('RemberAtLeastAfter')

    def run(self):
        while(True):
            path = os.getcwd()
            path = path + '\controllerProjectSelector.exe'
            subprocess.Popen([path])
            sleepTime = randint(int(self._minTime), int(self._maxTime))
            time.sleep(sleepTime)



tester = RememberingToolStarter()
tester.run()





