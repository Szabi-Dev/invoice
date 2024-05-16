

from services.config_parser import config_parser
from services.youtrack import sprint_service


config = config_parser.parse_project_config("src/config/dlouhy.ini");

url = config['YOUTRACK']['url']
projectId = config['YOUTRACK']['project']
token = config['YOUTRACK']['token'];

sprint_service.get_sprints(url,token, projectId);

