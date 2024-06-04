
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



def millisec_to_date_with_name_of_the_week(milliseconds):
    return millisec_to_date_with_format(milliseconds, "%Y-%m-%d %A")

def millisec_to_date_string(milliseconds):
    return millisec_to_date_with_format(milliseconds, "%Y-%m-%d")

def millisec_to_date_with_format(milliseconds, format):
    return datetime.fromtimestamp(milliseconds/1000.0).strftime(format) 