import csv
import os
from shutil import copy2

# ---Zu Debug-Zwecken. Gehört wieder entfernt----------------------------------------------------------------------------
#import logging
#
#logger = logging.getLogger('spam_application')
#logger.setLevel(logging.DEBUG)
## create file handler which logs even debug messages logger.info('end write')
#fh = logging.FileHandler('spam.log')
#fh.setLevel(logging.DEBUG)
#logger.addHandler(fh)


# -----------------------------------------------------------------------------------------------------------------------


class CsvWriter:
    def __init__(self, initialTime, timeStep):
        self._cwd = os.getcwd()
        self._timeStep = timeStep
        self._initialTime = initialTime
        self._projRunTime = 0.0
        self._currentProj = ""
        self.file_name = initialTime.month + initialTime.year + '.csv'
        self._folder = self._cwd + '\\' + self._initialTime.month + self._initialTime.year
        self._initialTime = initialTime
        self.fieldnames = ['Project']
        self._makeBackupFileIfExists()
        for i in range(1, 32):
            self.fieldnames.append(i)
        self.readData = dict(dict())

    def _makeBackupFileIfExists(self):
        self._createFolderIfNotExists()
        self._copyYesterdaysFileIfExists()

    def _createFolderIfNotExists(self):
        if not os.path.isdir(self._folder):
            try:
                os.makedirs(self._folder)
            except OSError:
                print("Creation of the directory %s failed" % self._folder)

    def _copyYesterdaysFileIfExists(self):
        filePath = self._cwd + '\\' + self.file_name
        dest = self._folder + '\\' + self._initialTime.day_of_month + self.file_name
        if os.path.isfile(filePath):
            copy2(filePath, dest)

    def write_current_time(self, currentProj):
        #logger.info('begin write_current_time')
        self._read()
        if not currentProj == self._currentProj:
            self._currentProj = currentProj
            self._projRunTime = self._getProjectsRuntime()
        self._projRunTime += self._timeStep / 3600
        if self._projRunTime > 0.01:
            try:
                open(self.file_name, "w+")
            except IOError:
                return
            self._write()
        #logger.info('end write_current_time')

    def _read(self):
        #logger.info('begin _read')
        try:
            open(self.file_name, "r+")
        except IOError:
            return
        with open(self.file_name) as csvfile:
            self.readData.clear()
            reader = csv.DictReader(csvfile, delimiter=";", fieldnames=self.fieldnames)
            for row in reader:
                if row['Project'] == 'Project' or row['Project'] == "":
                    continue
                row_data = dict()
                row_data['Project'] = row['Project']
                for i in range(1, 32):
                    row_data[i] = row[i]
                self.readData[row['Project']] = row_data
        #logger.info('end _read')

    def _appendRow(self):
        #logger.info('begin _appendRow')
        row_data = dict()
        for i in range(1, 32):
            row_data[i] = ""
        self.readData[self._currentProj] = row_data
        #logger.info('end _appendRow')

    def _getProjectsRuntime(self):
        #logger.info('begin _getProjectsRuntime')
        if self._currentProj in self.readData:
            if int(self._initialTime.day_of_month) in self.readData[self._currentProj]:
                if self.readData[self._currentProj][int(self._initialTime.day_of_month)] == '':
                    return 0.0
                return float(self.readData[self._currentProj][int(self._initialTime.day_of_month)])
            else:
                return 0.0
        else:
            return 0.0
        #logger.info('end _getProjectsRuntime')

    def _write(self):
        #logger.info('begin _write')
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=self.fieldnames)
            writer.writeheader()

            if self._currentProj not in self.readData:
                self._appendRow()

            self.readData[self._currentProj][int(self._initialTime.day_of_month)] = round(self._projRunTime, 2)

            for key, val in sorted(self.readData.items()):
                row = {'Project': key}
                row.update(val)
                writer.writerow(row)
        #logger.info('end _write')
