
import requests
from models.date.date_model import DateModel
from services.date.date_service import millisec_to_date_string, millisec_to_date_with_name_of_the_week
from services.url import url_builder


WORKITEM_URL =  "/workItems?"

PARAM_TOP = "$top";
PARAM_TOP_VALUE = 10000;

PARAM_FIELDS = "fields";
PARAM_FIELDS_VALUE = "created,duration(presentation,minutes),author(name),id,date,type(id,name)";

PARAM_AUTHOR="author"
PARAM_AUTHOR_VALUE = "me"

PARAM_START_DATE="startDate";
PARAM_END_DATE="endDate";


def get_workitems_for_sprint(youtrack_config, sprint):
    start_date = millisec_to_date_string(sprint['start']);
    end_date = millisec_to_date_string(sprint['finish']);
    return get_workitems_for_interval(youtrack_config, start_date, end_date);

def get_workitems_for_interval(youtrack_config, start_date, end_date):
    Headers = { "Authorization" : "Bearer " + youtrack_config.token }
    url = youtrack_config.url + WORKITEM_URL;
    url = url_builder.add_param_to_url(url, PARAM_FIELDS, str(PARAM_FIELDS_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_TOP, str(PARAM_TOP_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_AUTHOR, str(PARAM_AUTHOR_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_START_DATE, str(start_date));
    url = url_builder.add_param_to_url(url, PARAM_END_DATE, str(end_date));
    response = requests.get(url, headers=Headers);
    return response.json();

def calculate_workitem_duration_in_hours(workItems):
    allminutes = 0;
    for item in workItems:
        allminutes = allminutes + item['duration']['minutes'];
    return allminutes / 60;

def create_work_items_per_day_dict(workItems):
    workitems_per_day = {}
    for w in workItems:
        day = millisec_to_date_with_name_of_the_week(w['date'])
        if not day in workitems_per_day:
            workitems_per_day[day] = []
        workitems_per_day[day].append(w);
    return workitems_per_day;