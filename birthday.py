import datetime
users = [
    {'name': 'Ivan', 'birthday': datetime.datetime(year=1992, month=2, day=29)},

    {'name': 'Andrii', 'birthday': datetime.datetime(year=1986, month=11, day=8)},

    {'name': 'Semen', 'birthday': datetime.datetime(year=1989, month=11, day=10)},

    {'name': 'Serhii', 'birthday': datetime.datetime(year=1954, month=11, day=11)},

    {'name': 'Dmytro', 'birthday': datetime.datetime(year=1934, month=11, day=14)},

    {'name': 'Oleksii', 'birthday': datetime.datetime(year=1954, month=11, day=6)},

    {'name': 'Inna', 'birthday': datetime.datetime(year=1954, month=11, day=8)}
]

def convert_to_current_year(users): #фунція видає день народження працівника в цьому році та корегує її на випадок ДН, яке припадає на 29 лютого, у випадку, якщо цей рік не є високосним.
    for user in users:
        date = user['birthday']
        day = date.day
        month = date.month
        try:
            birthdate_this_year = datetime.datetime(year=2022, month=month, day=day)
            update_pair = {'birthday': birthdate_this_year}
            user.update(update_pair)
        except ValueError:
            month = 3
            day = 1
            birthdate_this_year = datetime.datetime(year=2022, month=month, day=day)
            update_pair = {'birthday': birthdate_this_year}
            user.update(update_pair)
    return users


def define_range(current_date): #фунція не включає в діапазон зайві вихідні дні наступного тижня, якщо програма запущена у вихідний день поточного
    if current_date.weekday() == 5:
        range = datetime.timedelta(days=6)
    elif current_date.weekday() == 5:
        range = datetime.timedelta(days=5)
    else:
        range = datetime.timedelta(days=7)
    return range


def get_birthdays_per_week(users): #фінальна функція

    days = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    birthdays = convert_to_current_year(users)
    current_date = datetime.datetime.now()
    range = define_range(current_date)
    last_day_in_range = current_date + range

    for user in birthdays:
        birthday = user['birthday']
        if current_date < birthday <= last_day_in_range:
            weekday = birthday.strftime('%A')
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            days.get(weekday).append(user.get('name'))

    for k, v in days.items():
        print(f"{k}: {', '.join(v)}")


get_birthdays_per_week(users)
