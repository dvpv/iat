from typing import List
import yaml
import os
import re

from src.operations.operation import Operation
from src.operations.tint import Tint
from src.operations.zoom import Zoom
from src.operations.crop import Crop
from src.operations.rotation import Rotation
from src.models.config import Config

DEFAULT_SAVE_EACH_STEP_CONFIG = False


def parse_operation_from_dict(dictionary: dict) -> Operation:
    if "type" not in dictionary or type(dictionary["type"]) is not str:
        raise Exception("Invalid config file")
    operation_type = dictionary["type"]
    save = False
    if "save" in dictionary and type(dictionary["save"]) is bool:
        save = dictionary["save"]
    if operation_type.lower() == "tint":
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
    elif operation_type.lower() == "zoom":
        if "fx" not in dictionary:
            raise Exception("Invalid config file. Missing 'fx' attribute for Zoom.")
        elif type(dictionary["fx"]) not in [float, int]:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'fx' attribute (type must be float or int)."
            )
        if "fy" not in dictionary:
            raise Exception("Invalid config file. Missing 'fy' attribute for Zoom.")
        elif type(dictionary["fy"]) not in [float, int]:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'fy' attribute (type must be float or int)."
            )
        return Zoom(dictionary["fx"], dictionary["fy"], save_result=save)
    elif operation_type.lower() == "crop":
        if "x" not in dictionary:
            raise Exception("Invalid config file. Missing 'x' attribute for Crop.")
        elif type(dictionary["x"]) is not int:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'x' attribute (type must be int)."
            )
        if "y" not in dictionary:
            raise Exception("Invalid config file. Missing 'y' attribute for Crop.")
        elif type(dictionary["y"]) is not int:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'y' attribute (type must be int)."
            )
        return Crop([dictionary["x"], dictionary["y"]], save_result=save)
    elif operation_type.lower() == "rotation":
        if "degrees" not in dictionary:
            raise Exception(
                "Invalid config file. Missing 'degrees' attribute for Rotation."
            )
        elif type(dictionary["degrees"]) not in [int, float]:
            raise Exception(
                "Invalid config file. "
                "Invalid type of 'degrees' attribute (type must be float or int)."
            )
        return Rotation(int(dictionary["degrees"]), save_result=save)

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
    if "save_each_step" in config_dict:
        save_each_step = config_dict["save_each_step"]
    operations[-1].save_result = True
    config = Config(
        operations=operations,
        save_each_step=save_each_step,
    )

    return config


def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def get_file_type(file_name: str) -> str:
    return re.split("\\.", file_name)[-1]


def append_to_image_name(name: str, string: str) -> str:
    file_type = get_file_type(name)
    file_name = name[0 : len(name) - len(file_type) - 1]
    return f"{file_name}{string}.{file_type}"
