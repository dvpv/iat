import argparse
import sys
import cv2
import numpy as np
from models.image import Image
import cli

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
    default=sys.stdin,
    help="path to the input file",
)

parser.add_argument(
    "output",
    nargs="?",
    type=str,
    default=sys.stdout,
    help="path to the output file",
)

args = parser.parse_args()

print(args.config)
print(args.gui)
print(args.input)
print(args.output)

if args.gui:
    # running GUI
    print("Not implemented yet")
    pass
else:
    # running CLI
    cli.run_cli()
