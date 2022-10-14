import sys
import cv2
from src.models.config import Config
from src.models.image import Image
from src.process.process import *


def run(input_path: str, output_dir: str, config: Config) -> None:
    image_path = input_path if input_path != sys.stdin else sys.stdin.read()
    image = Image(image=cv2.imread(image_path, cv2.IMREAD_COLOR), path=image_path)
    process(image, config, output_dir)
