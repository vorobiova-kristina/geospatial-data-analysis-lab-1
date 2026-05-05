from datetime import date
from dateutil.relativedelta import relativedelta

def is_it_your_birthday(byear: int, bmonth: int, bday: int) -> str:
    bdate = date(byear, bmonth, bday)
    current_date = date.today()

    if bdate.strftime("%m-%d") == current_date.strftime("%m-%d"):
        print(f"Yay! Happy {relativedelta(current_date, bdate).years}th birhday")
    else:
        print(f"Too bad! Better luck next time")