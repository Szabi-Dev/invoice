

from services.config_parser import config_parser
from services.date.date_service import get_monthly_date_interval, millisec_to_date_string
from services.youtrack import sprint_service
from services.youtrack.workitem_service import calculate_workitem_duration_in_hours, get_workitems_for_sprint

config = config_parser.parse_youtrack_config("src/config/dlouhy.ini");

print('Year:')
year = int(input())
print('Month:')
month = int(input())

date = get_monthly_date_interval(year,month);
sprints = sprint_service.get_sprints_in_interval(config, date);

allhours = 0;
for sp in sprints:
    workitems = get_workitems_for_sprint(config, sp);
    durationInHours = calculate_workitem_duration_in_hours(workitems);
    allhours += durationInHours;
    print (sp['name'] + ": " + str(durationInHours) + "h  (" + millisec_to_date_string(sp['start']) + " - " + millisec_to_date_string(sp['finish']) + ")"  )

print("All: " + str(allhours) + "h ")




