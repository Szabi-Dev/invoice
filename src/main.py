

from services.config_parser import config_parser
from services.date.date_service import get_monthly_date_interval
from services.youtrack import sprint_service


config = config_parser.parse_youtrack_config("src/config/dlouhy.ini");


date = get_monthly_date_interval(2024,5);
sprints = sprint_service.get_sprints_in_interval(config, date);
print(sprints);



