import cv2
from typing import List
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class GaussianBlur(Operation):
    TYPE = "gaussianBlur"

    def from_dict(d: dict) -> Operation:
        return GaussianBlur(
            sigma=extract_key("sigma", d, [int]),
            save_result=extract_save(d),
        )

    def __init__(self, sigma: int, save_result: bool = False):
        self.__sigma = sigma
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.GaussianBlur(image, sigmaX=self.__sigma)
        return image
