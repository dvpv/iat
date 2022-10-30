from typing import List

import cv2
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Zoom(Operation):
    TYPE = "zoom"

    def from_dict(d: dict) -> Operation:
        return Zoom(
            fx=extract_key("fx", d, [int, float]),
            fy=extract_key("fy", d, [int, float]),
            save_result=extract_save(d),
        )

    def __init__(self, fx: float, fy: float, save_result: bool):
        self.__fx = fx
        self.__fy = fy
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.resize(image.image, None, fx=self.__fx, fy=self.__fy)
        return image
