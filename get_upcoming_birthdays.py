from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()

    birthdays = []

    for user in users:
        date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if date.year < today.year:
            birthday = date.replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if today <= birthday <= today + timedelta(days=7):
            if 5 <= birthday.weekday() <= 6:
                birthday += timedelta(days=(7 - birthday.weekday()))

            birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday.strftime('%Y.%m.%d')
            })

    return birthdays
