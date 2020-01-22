from os import path

import projSelectorUi
import time


def getProjList():
    file_path = path.relpath("internal/projectList.tmc")
    with open(file_path) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def setProjList(projList):
    file_path = path.relpath("internal/projectList.tmc")
    with open(file_path, 'w') as f:
        for item in projList:
            f.write("%s\n" % item)


def getCurrentProj():
    file_path = path.relpath("internal/CurrentProject.tmc")
    file = open(file_path)
    return file.readline()


def saveCurrentProj(proj):
    file_path = path.relpath("internal/CurrentProject.tmc")
    with open(file_path, 'w') as the_file:
        the_file.write(proj)


class Controller:
    def __init__(self):
        self._projList = getProjList()
        self._currProj = getCurrentProj()
        if self._currProj not in self._projList:
            self._projList.append(self._currProj)
        self._ui = projSelectorUi.ProjSelectorUi(self._currProj, self._projList)
        self._ui.callbackOkay = self._onOkay

    def run(self):
        if not projSelectorUi.deleteme(self._currProj):
            self._ui.run()

    def _wait_if_necessary(self):
        duration = self._ui.get_duration()
        if duration is not 'aus':
            time.sleep(float(duration)*3600)
            saveCurrentProj(self._currProj)

    def _onOkay(self):
        selected_project = self._ui.getSelectedProj()
        saveCurrentProj(selected_project)
        setProjList(self._ui.getProjList())

        self._wait_if_necessary()


controller = Controller()
controller.run()
