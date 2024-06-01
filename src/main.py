

from services.config_parser import config_parser
from services.youtrack import sprint_service


config = config_parser.parse_youtrack_config("src/config/dlouhy.ini");

sprints = sprint_service.get_sprints(config);



