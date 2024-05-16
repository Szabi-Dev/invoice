import configparser
import os;

PROJECT_PATH = "src/config/";


def parse_project_config(config_path):
    project_path = os.path.join(os.getcwd(), config_path)
    return parse_config(project_path);

def parse_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path);
    return config;