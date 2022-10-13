from algorithms.algorithm import Algorithm
from models.image import Image


class Tint(Algorithm):
    def __init__(self, color: str, save_result: bool = False):
        self.__color = color
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        # TODO: implement tint
        return image
