import yaml
import os
import re

from algorithms.algorithm import Algorithm
from algorithms.tint import Tint
from models.config import Config

DEFAULT_SAVE_EACH_STEP_CONFIG = False


def parse_operation_from_dict(dictionary: dict) -> Algorithm:
    if "type" not in dictionary or type(dictionary["type"]) is not str:
        raise "Invalid config file"
    operation_type = dictionary["type"]
    save = False
    if "save" in dictionary and type(dictionary["save"]) is bool:
        save = dictionary["save"]
    if operation_type == "tint":
        if "color" not in dictionary:
            raise "Invalid config file"
        return Tint(dictionary["color"], save_result=save)

    raise "Invalid config file. Unknown operation type."


def parse_config_file(path: str) -> Config:
    stream = open(path, "r")
    config_dict = yaml.safe_load(stream)
    operations = []
    if "operations" in config_dict and type(config_dict["operations"]) is list:
        for operation in config_dict["operations"]:
            operations.append(parse_operation_from_dict(operation))
    else:
        raise "Invalid config file"

    save_each_step = DEFAULT_SAVE_EACH_STEP_CONFIG
    if save_each_step in config_dict:
        save_each_step = config_dict["save_each_step"]
    operations[-1].save_result = True
    config = Config(
        operations=operations,
        save_each_step=save_each_step,
    )

    return config


def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def append_to_image_name(name: str, string: str) -> str:
    file_type = re.split("\\.", name)[-1]
    file_name = name[0 : len(name) - len(file_type) - 1]
    return f"{file_name}{string}.{file_type}"
