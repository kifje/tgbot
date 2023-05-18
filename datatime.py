import datetime

async def get_today():
    today_str = datetime.datetime.today().strftime('%d.%m.%Y')
    return today_str

async def get_tomorrow():
    delta = datetime.timedelta(days=1)
    today = datetime.datetime.today()
    nextday_str = (today+delta).strftime('%d.%m.%Y')
    return nextday_str
