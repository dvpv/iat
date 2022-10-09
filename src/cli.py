import sys
import cv2
import numpy as np
from models.image import Image


def run_cli(args) -> None:
    image_path = args.input if args.input != sys.stdin else sys.stdin.read()
    image = Image(image=cv2.imread(image_path, cv2.IMREAD_COLOR), path=image_path)
