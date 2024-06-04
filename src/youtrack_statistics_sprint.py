

from services.config_parser import config_parser
from services.date.date_service import millisec_to_date_string, millisec_to_date_with_name_of_the_week
from services.youtrack import sprint_service
from services.youtrack.workitem_service import calculate_workitem_duration_in_hours, get_workitems_for_sprint

config = config_parser.parse_youtrack_config("src/config/dlouhy.ini");

print('Sprint')
sprintNumber = str(input())

sprint = sprint_service.get_sprint(config, sprintNumber)
workItems = get_workitems_for_sprint(config, sprint)


workitems_per_day = {}

for w in workItems:
    day = millisec_to_date_with_name_of_the_week(w['date'])
    if not day in workitems_per_day:
        workitems_per_day[day] = []
    workitems_per_day[day].append(w);


allhours = 0;
for key in workitems_per_day:
    durationInHours = calculate_workitem_duration_in_hours(workitems_per_day[key]);
    allhours += durationInHours;
    print(key + ": " + str(durationInHours) + "h ")


print("All: " + str(allhours) + "h")