from typing import List

import cv2
from src.operations.crop import Crop
from src.operations.operation import Operation
from src.models.image import Image


class Zoom(Operation):
    def __init__(self, fx: float, fy: float, save_result: bool):
        self.__fx = fx
        self.__fy = fy
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.resize(image.image, None, fx=self.__fx, fy=self.__fy)
        return image
