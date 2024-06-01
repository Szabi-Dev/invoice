
import requests
from services.url import url_builder


WORKITEM_URL =  "/workItems?"

PARAM_TOP = "$top";
PARAM_TOP_VALUE = 10000;

PARAM_FIELDS = "fields";
PARAM_FIELDS_VALUE = "created,duration(presentation,minutes),author(name),id";

PARAM_AUTHOR="author"
PARAM_AUTHOR_VALUE = "me"

PARAM_START_DATE="startDate";
PARAM_END_DATE="endDate";


def get_workitems_for_interval(youtrack_config, datemodel):
    Headers = { "Authorization" : "Bearer " + youtrack_config.token }
    url = youtrack_config.url + WORKITEM_URL;
    url = url_builder.add_param_to_url(url, PARAM_FIELDS, str(PARAM_FIELDS_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_TOP, str(PARAM_TOP_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_AUTHOR, str(PARAM_AUTHOR_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_START_DATE, str(datemodel.start_in_ms));
    url = url_builder.add_param_to_url(url, PARAM_END_DATE, str(datemodel.end_in_ms));
    response = requests.get(url, headers=Headers);
    return response.json();