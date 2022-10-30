import yaml
import os
import re
from src.operations.blur import Blur
from src.operations.operation import Operation
from src.operations.gaussian_blur import GaussianBlur
from src.operations.tint import Tint
from src.operations.zoom import Zoom
from src.operations.crop import Crop
from src.operations.rotation import Rotation
from src.models.config import Config

DEFAULT_SAVE_EACH_STEP_CONFIG = False


def parse_operation(d: dict) -> Operation:
    if "type" not in d or type(d["type"]) is not str:
        raise Exception("Invalid config file")
    operation_type: str = d["type"]
    match operation_type:
        case Crop.TYPE:
            return Crop.from_dict(d)
        case GaussianBlur.TYPE:
            return GaussianBlur.from_dict(d)
        case Rotation.TYPE:
            return Rotation.from_dict(d)
        case Tint.TYPE:
            return Tint.from_dict(d)
        case Zoom.TYPE:
            return Zoom.from_dict(d)
        case Blur.TYPE:
            return Blur.from_dict(d)
        case _:
            raise Exception(f"Unknown type {operation_type}")


def parse_config_file(path: str) -> Config:
    stream = open(path, "r")
    config_dict = yaml.safe_load(stream)
    operations = []
    if "operations" in config_dict and type(config_dict["operations"]) is list:
        for operation in config_dict["operations"]:
            operations.append(parse_operation(operation))
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
