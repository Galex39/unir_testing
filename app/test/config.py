import yaml
from typing import Dict


def init_config() -> Dict:
    with open("./app/config/config.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data


config = init_config()
