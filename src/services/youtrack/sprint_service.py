import requests
from services.url import url_builder


SPRINT_URL =  "/agiles/{projectId}/sprints?"

PARAM_TOP = "top";
PARAM_TOP_VALUE = 1000;

PARAM_FIELDS = "fields"; 
PARAM_FIELDS_VALUE = "id,name,start,finish";



def get_sprints(youtrack_config):
    postfix = SPRINT_URL.replace("{projectId}", str(youtrack_config.project));
    Headers = { "Authorization" : "Bearer " + youtrack_config.token }
    url = youtrack_config.url + postfix;
    url = url_builder.add_param_to_url(url, PARAM_FIELDS, str(PARAM_FIELDS_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_TOP, str(PARAM_TOP_VALUE));
    response = requests.get(url, headers=Headers);
    print(response.json());
