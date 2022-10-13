import yaml
import os
import re


def get_yaml_config(path: str):
    pass


def get_absolute_path(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def append_to_image_name(name: str, string: str) -> str:
    file_type = re.split("\\.", name)[-1]
    file_name = name[0 : len(name) - len(file_type) - 1]
    return f"{file_name}{string}.{file_type}"
