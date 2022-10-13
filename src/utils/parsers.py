from typing import List
import yaml
import os
import re

from src.algorithms.algorithm import Algorithm
from src.algorithms.tint import Tint
from src.models.config import Config

DEFAULT_SAVE_EACH_STEP_CONFIG = False


def parse_operation_from_dict(dictionary: dict) -> Algorithm:
    if "type" not in dictionary or type(dictionary["type"]) is not str:
        raise Exception("Invalid config file")
    operation_type = dictionary["type"]
    save = False
    if "save" in dictionary and type(dictionary["save"]) is bool:
        save = dictionary["save"]
    if operation_type == "tint":
        if "color" not in dictionary:
            raise Exception("Invalid config file. Missing 'color' attribute for Tint.")
        elif (
            type(dictionary["color"]) is not list
            or type(dictionary["color"][0]) is not int
        ):
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'color' attribute (type must be List[int])."
            )
        elif len(dictionary["color"]) != 3:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'color' attribute (len must be 3)."
            )
        return Tint(dictionary["color"], save_result=save)

    raise Exception("Invalid config file. Unknown operation type.")


def parse_config_file(path: str) -> Config:
    stream = open(path, "r")
    config_dict = yaml.safe_load(stream)
    operations = []
    if "operations" in config_dict and type(config_dict["operations"]) is list:
        for operation in config_dict["operations"]:
            operations.append(parse_operation_from_dict(operation))
    else:
        raise Exception("Invalid config file")

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
