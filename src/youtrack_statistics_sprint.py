

from services.config_parser import config_parser
from services.date.date_service import millisec_to_date_string, millisec_to_date_with_name_of_the_week
from services.youtrack import sprint_service
from services.youtrack.workitem_service import calculate_workitem_duration_in_hours, create_work_items_per_day_dict, get_workitems_for_sprint

config = config_parser.parse_youtrack_config("src/config/dlouhy.ini");

print('Sprint')
sprintNumber = str(input())

sprint = sprint_service.get_sprint(config, sprintNumber)
workItems = get_workitems_for_sprint(config, sprint)


workitems_per_day = create_work_items_per_day_dict(workItems);


allhours = 0;
for key in workitems_per_day:
    durationInHours = calculate_workitem_duration_in_hours(workitems_per_day[key]);
    allhours += durationInHours;
    print(key + ": " + str(durationInHours) + "h ")


print("All: " + str(allhours) + "h")