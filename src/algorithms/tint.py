import numpy as np
import cv2
from typing import List
from src.algorithms.algorithm import Algorithm
from src.models.image import Image


class Tint(Algorithm):
    def __init__(self, color: List[int], save_result: bool = False):
        self.__color = [255 if val > 255 else val for val in color]
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        overlay = np.full(image.image.shape, self.__color, np.uint8)
        image.image = cv2.add(image.image, overlay)
        return image
