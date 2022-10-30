import cv2
from typing import List
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Blur(Operation):
    TYPE = "blur"

    def from_dict(d: dict) -> Operation:
        return Blur(
            ksize=extract_key("ksize", d, [list]),
            save_result=extract_save(d),
        )

    def __init__(self, ksize: List[int], save_result: bool = False):
        self.__ksize = ksize
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.blur(image.image, self.__ksize)
        return image
