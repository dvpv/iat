import cv2
import numpy as np
from typing import List
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Erode(Operation):
    TYPE = "erode"

    def from_dict(d: dict) -> Operation:
        return Erode(
            ksize=extract_key("ksize", d, [list]),
            iterations=extract_key("iterations", d, [int], default_value=1),
            save_result=extract_save(d),
        )

    def __init__(self, ksize: List[int], iterations: int, save_result: bool = False):
        self.__ksize = ksize
        self.__iterations = iterations
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        kernel = np.ones(self.__ksize, np.uint8)
        image.image = cv2.erode(image.image, kernel, iterations=self.__iterations)
        return image
