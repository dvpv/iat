import json
from typing import List
import yaml
import os
import re
from src.operations import *

DEFAULT_SAVE_EACH_STEP_CONFIG = False


def parse_operation(d: dict, macros: List[Operation]) -> Operation:
    operation_type = extract_key("type", d, [str])
    if operation_type in [macro.TYPE for macro in macros]:
        return next(m for m in macros if m.TYPE == operation_type)
    operations = Operation.__subclasses__()
    operations = [
        operation for operation in operations if operation.__name__ != "Macro"
    ]
    for operation in operations:
        if operation_type == operation.TYPE:
            return operation.from_dict(d)
    raise Exception(f"Unknown type {operation_type}")


def read_config_yaml(path: str) -> dict:
    return yaml.safe_load(open(path, "r"))


def read_config_json(path: str) -> dict:
    return json.load(open(path, "r"))


def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def get_file_type(file_name: str) -> str:
    return re.split("\\.", file_name)[-1]


def append_to_image_name(name: str, string: str) -> str:
    file_type = get_file_type(name)
    file_name = name[0 : len(name) - len(file_type) - 1]
    return f"{file_name}{string}.{file_type}"
