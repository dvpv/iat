import numpy as np
import cv2
from typing import List
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Tint(Operation):
    TYPE = "tint"

    def from_dict(d: dict) -> Operation:
        return Tint(
            color=extract_key("color", d, [list]),
            save_result=extract_save(d),
        )

    def __init__(self, color: List[int], save_result: bool = False):
        self.__color = [
            -255 if v < -255 else v
            for v in [255 if val > 255 else val for val in color]
        ]
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        overlay = np.full(image.image.shape, self.__color, np.uint8)
        image.image = cv2.add(image.image, overlay)
        return image
