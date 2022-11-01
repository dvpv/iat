import argparse
from base64 import encode

from yaml import parse
from src.utils.parsers import *
import src.cli as cli
from src.gui.app import App
from src.models.config import Config

DEFAULT_CONFIG_LOCATION = "./config.yaml"

parser = argparse.ArgumentParser(description="Image Augmentation Tool")

parser.add_argument(
    "-c",
    "--config",
    type=str,
    default=DEFAULT_CONFIG_LOCATION,
    help="path to the configuration file",
)

parser.add_argument(
    "-g",
    "--gui",
    "--GUI",
    action="store_true",
    help="run with GUI",
)

parser.add_argument(
    "input",
    nargs="?",
    type=str,
    help="path to the input file",
)

parser.add_argument(
    "output",
    nargs="?",
    type=str,
    help="path to the output dir",
)

args = parser.parse_args()


config_dict = read_config_yaml(args.config)
output_dir = None
if args.output != None:
    output_dir = get_absolute_path(args.output)
config = Config.from_dict(config_dict, output_dir)
if args.gui:
    # running GUI
    app = App(config, output_dir)
    app.run()
else:
    # running CLI
    input_path = get_absolute_path(args.input)
    cli.run(input_path, output_dir, config)
