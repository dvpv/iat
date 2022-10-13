import argparse
from src.utils.parsers import *
import src.cli as cli

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

# TODO: remove
print(args.config)
print(args.gui)
print(args.input)
print(args.output)
# END TODO

if args.gui:
    # running GUI
    # TODO: implement gui
    print("Not implemented yet")
    pass
else:
    # running CLI
    config = parse_config_file(args.config)
    input_path = get_absolute_path(args.input)
    output_dir = get_absolute_path(args.output)
    cli.run(input_path, output_dir, config)
