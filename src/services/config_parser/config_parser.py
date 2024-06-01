import configparser
import os

from models.config.youtrack_config_model import YoutrackConfigModel;

PROJECT_PATH = "src/config/";


def parse_youtrack_config(config_path):
    config = parse_project_config(config_path);
    return YoutrackConfigModel(
      config['YOUTRACK']['url'],
      config['YOUTRACK']['project'],
      config['YOUTRACK']['token']
    );


def parse_project_config(config_path):
    project_path = os.path.join(os.getcwd(), config_path)
    return parse_config(project_path);

def parse_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path);
    return config;