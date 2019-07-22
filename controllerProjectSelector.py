from os import path

import projSelectorUi


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

    def _onOkay(self):
        saveCurrentProj(self._ui.getSelectedProj())
        setProjList(self._ui.getProjList())


controller = Controller()
controller.run()
