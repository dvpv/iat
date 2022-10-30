import cv2
from typing import List
from src.operations.operation import Operation
from src.models.image import Image


class GaussianBlur(Operation):
    def __init__(self, sigma: int, save_result: bool = False):
        self.__sigma = sigma
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.GaussianBlur(image, sigmaX=self.__sigma)
        return image
