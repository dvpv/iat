from src.algorithms.algorithm import Algorithm
from src.models.image import Image


class Crop(Algorithm):
    def __init__(self, dimensions: list[float, float]):
        self.__dimensions = dimensions

    def process(self, image: Image) -> Image:
        # TODO: implement crop
        return image
