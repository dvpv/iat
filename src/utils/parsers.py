import yaml
import os
import re
from src.operations.gamma_correction import GammaCorrection
from src.operations.resize import Resize
from src.operations.blur import Blur
from src.operations.operation import Operation
from src.operations.gaussian_blur import GaussianBlur
from src.operations.tint import Tint
from src.operations.zoom import Zoom
from src.operations.crop import Crop
from src.operations.rotation import Rotation

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
        case Resize.TYPE:
            return Resize.from_dict(d)
        case GammaCorrection.TYPE:
            return GammaCorrection.from_dict(d)
        case _:
            raise Exception(f"Unknown type {operation_type}")


def read_config_yaml(path: str) -> dict:
    return yaml.safe_load(open(path, "r"))


def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def get_file_type(file_name: str) -> str:
    return re.split("\\.", file_name)[-1]


def append_to_image_name(name: str, string: str) -> str:
    file_type = get_file_type(name)
    file_name = name[0 : len(name) - len(file_type) - 1]
    return f"{file_name}{string}.{file_type}"
