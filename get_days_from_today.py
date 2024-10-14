from datetime import datetime

def get_days_from_today(date: str)->int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        days =today - date
        return days.days
    except:
        print("wrong date")
        return 0

