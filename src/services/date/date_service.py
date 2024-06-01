
from datetime import datetime

from models.date.date_model import DateModel


def get_monthly_date_interval(year, month):
    start_dt_string = '1.' + str(month) + '.' + str(year);
    if month == 12:
        year = year + 1;
        month = 0;
    end_dt_string = '1.' + str(month+1) + '.' + str(year);
    return DateModel(
        date_string_to_millisec(start_dt_string),
        date_string_to_millisec(end_dt_string)
    )

def date_string_to_millisec(date_string):
    dt = datetime.strptime(date_string,'%d.%m.%Y');
    return dt.timestamp() * 1000;    