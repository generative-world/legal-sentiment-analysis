import os
import yaml

CONFIG_PATH = "config/config.yml"

def load_config():
    try:
        with open(CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception("Configuration file not found!")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")

config = load_config()
DB_CONFIG = config.get("DB", {})
AWS_CONFIG = config.get("AWS", {})
