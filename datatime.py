import datetime

async def get_today():
    today_str = datetime.datetime.today().strftime('%d.%m')
    return today_str

async def get_tomorrow():
    delta = datetime.timedelta(days=1)
    today = datetime.datetime.today()
    nextday_str = (today+delta).strftime('%d.%m')
    return nextday_str

async def get_week():
    today = datetime.datetime.today()
    tweek = (datetime.date(today.year, today.month, today.day).isocalendar().week)
    return tweek

async def get_dweek():
    today = datetime.date.today()
    days = today.weekday()
    # day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
    # daystr = day[days]
    return days
