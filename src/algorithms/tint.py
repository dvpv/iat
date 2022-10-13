from algorithms.algorithm import Algorithm
from models.image import Image


class Tint(Algorithm):
    def __init__(self, color):
        self.__color = color

    def process(self, image: Image) -> Image:
        # TODO: implement tint
        return image
