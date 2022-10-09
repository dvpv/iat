import argparse
import sys

parser = argparse.ArgumentParser(description="Image Augmentation Tool")

parser.add_argument(
    "-c",
    "--config",
    type=str,
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
    type=argparse.FileType("r"),
    default=sys.stdin,
    help="path to the input file",
)

parser.add_argument(
    "outfile",
    nargs="?",
    type=argparse.FileType("w"),
    default=sys.stdout,
    help="path to the output file",
)

args = parser.parse_args()

print(args.config)
print(args.gui)
print(args.input)
print(args.output)
