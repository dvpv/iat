import sys
import os
import cv2
from src.models.config import Config
from src.models.image import Image


def run(input_path: str, output_dir: str, config: Config) -> None:
    image_path = input_path if input_path != sys.stdin else sys.stdin.read()
    if not os.path.isfile(image_path):
        raise Exception(f"Image {image_path} not found")
    image = Image(image=cv2.imread(image_path, cv2.IMREAD_COLOR), path=image_path)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    config.process_image(image, output_dir)
