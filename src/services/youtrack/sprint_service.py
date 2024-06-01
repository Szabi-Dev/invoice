import requests
from services.url import url_builder


SPRINT_URL =  "/agiles/{projectId}/sprints?"

PARAM_TOP = "$top";
PARAM_TOP_VALUE = 1000;

PARAM_FIELDS = "fields"; 
PARAM_FIELDS_VALUE = "id,name,start,finish";

def get_sprints_in_interval(youtrack_config, datemodel):
    response = get_sprints(youtrack_config);
    sprints = [];

    for e in response:
        if e['finish'] != None and e['start'] < datemodel.end_in_ms and e['finish'] > datemodel.start_in_ms:
            sprints.append(e);
    sprints.sort(key=sortSprint);
    sprints[0]['start'] = datemodel.start_in_ms;
    sprints[-1]['finish'] = datemodel.end_in_ms;
    for sp in sprints:
        sp['finish'] = sp['finish'] - 86400000;
    return sprints;  

def get_sprints(youtrack_config):
    postfix = SPRINT_URL.replace("{projectId}", str(youtrack_config.project));
    Headers = { "Authorization" : "Bearer " + youtrack_config.token }
    url = youtrack_config.url + postfix;
    url = url_builder.add_param_to_url(url, PARAM_FIELDS, str(PARAM_FIELDS_VALUE));
    url = url_builder.add_param_to_url(url, PARAM_TOP, str(PARAM_TOP_VALUE));
    print(url)
    response = requests.get(url, headers=Headers);
    return response.json();

def sortSprint(e):
    return e['start']


