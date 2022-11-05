import datetime

def get_birthdays_per_week(users):
    days = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }
    res = {}
    today = datetime.datetime.now()
    one_week_forward = today + datetime.timedelta(days=7)
    user = {'Andrii': datetime.datetime(year=2022, month=11, day=8)}
    ts_today = today.timestamp()
    ts_week_forward = one_week_forward.timestamp()
    for user in users:
        for k, v in user.items():
            if ts_today <= v.timestamp() and v.timestamp() <= ts_week_forward:
                if v.weekday() == 0:
                    days['Monday'] = k + ',' + ' '
                elif v.weekday() == 1:
                    days['Tuesday'] += k + ',' + ' '
                elif v.weekday() == 2:
                    days['Wednesday'] = k + ',' + ' '
                elif v.weekday() == 3:
                    days['Thursday'] = k + ',' + ' '
                elif v.weekday() == 4:
                    days['Friday'] = k + ',' + ' '
                else:
                    days['Monday'] = k + ',' + ' '
    for key in days:
        if len(days[key]) >= 1:
            res[key] = days[key][:-2]
    for key, value in res.items():
        print(key + " : " + value)





users = [
    {'Ivan': datetime(year=2022, month=10, day=12)},

    {'Andrii': datetime(year=2022, month=11, day=8)},

    {'Ivan': datetime(year=2022, month=11, day=10)},
]
get_birthdays_per_week(users)