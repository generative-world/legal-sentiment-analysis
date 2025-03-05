import os
import yaml

CONFIG_PATH = "config/config.yml"

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()

DB_CONFIG = config["DB"]
AWS_CONFIG = config["AWS"]
