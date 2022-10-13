import sys
import cv2
import numpy as np
from algorithms.tint import Tint
from models.image import Image
from process.process import *


def run(input_path: str, output_dir: str) -> None:
    image_path = input_path if input_path != sys.stdin else sys.stdin.read()
    image = Image(image=cv2.imread(image_path, cv2.IMREAD_COLOR), path=image_path)
    algo = Tint("#101010")  # TODO: replace
    algo.save_result = True  # TODO: replace
    process(image, [algo, algo, algo], output_dir)
