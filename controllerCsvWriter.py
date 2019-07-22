import re
import csvFileWriter
import time
import timeData
import datetime

from os import path

time_step = 60  # in seconds

firstBreakBegin = 3600 * 6  # in seconds
firstBreakEnd = 3600 * 6.5
secondBreakBegin = 3600 * 9
secondBreakEnd = 3600 * 9.25


def getCurrentProj():
    file_path = path.relpath("internal/currentProject.tmc")
    file = open(file_path)
    return file.readline()

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x

def getStartupTime():
    file_path = path.relpath("internal/startup.tmc")

    now = timeData.get_time_date()

    with open(file_path, 'r+') as startupFile:
        for date_time_str in startupFile:
            date_time_str = chomp(date_time_str)
            try:
                datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
            except:
                continue
            then = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
            then = timeData.get_time_date_from(then)
            if timeData.getDurationInHours(now, then) < 10:
                return then

        startupFile.write("%s\n" % now.date)
        return now


def getRuntime():
    start_time = getStartupTime()
    now = timeData.get_time_date()
    return timeData.getDurationInSeconds(now, start_time)


class Controller:
    def __init__(self):
        self.start_time = getStartupTime()
        self._writer = csvFileWriter.CsvWriter(self.start_time, time_step)

    def run(self):
        timecounter = getRuntime()
        while True:
            time.sleep(time_step)

            timecounter += time_step
            if self._isPause(timecounter):
                self._writer.write_current_time("Pause")
            else:
                self._writer.write_current_time(getCurrentProj())

            if timecounter > 3600 * (10 + 0.75):  # stop after 10 hours + pause
                break

    def _isPause(self, timecounter):
        if firstBreakBegin <= timecounter < firstBreakEnd or \
                secondBreakBegin <= timecounter < secondBreakEnd:
            return True
        return False


controller = Controller()
controller.run()
