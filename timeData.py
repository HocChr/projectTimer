import datetime


class time_data:
    date = 0
    year = ''
    month = ''
    day_of_month = ''
    monthNr = ''
    day = ''
    hour = ''
    minute = ''

def get_time_date():
    time_ = time_data()
    time_.date         = datetime.datetime.now()
    time_.year         = time_.date.strftime('%Y')
    time_.month        = time_.date.strftime('%B')
    time_.monthNr      = time_.date.strftime('%m')
    time_.day_of_month = time_.date.strftime('%d')
    time_.day          = time_.date.strftime("%A")
    time_.hour         = time_.date.strftime('%H')
    time_.minute       = time_.date.strftime('%M')
    return time_

def get_time_date_from(date):
    time_ = time_data()
    time_.date         = date
    time_.year         = time_.date.strftime('%Y')
    time_.month        = time_.date.strftime('%B')
    time_.monthNr      = time_.date.strftime('%m')
    time_.day_of_month = time_.date.strftime('%d')
    time_.day          = time_.date.strftime("%A")
    time_.hour         = time_.date.strftime('%H')
    time_.minute       = time_.date.strftime('%M')
    return time_

# -returns 0 if days differ
def getDurationInSeconds(time1, time2):
    duration = time1.date - time2.date
    return duration.seconds

def getDurationInDays(time1, time2):
    duration = time1.date - time2.date
    days = duration.days
    return days

def getDurationInHours(time1, time2):
    seconds = getDurationInSeconds(time1, time2)
    days = getDurationInDays(time1, time2)
    hours = divmod(seconds, 3600)[0]
    return (days*24) + hours

def format_data(data):
    formated_data = [list()]
    i = 0
    while i < len(data):
        pass
    return formated_data
