from algorithms.algorithm import Algorithm
from models.image import Image


class Zoom(Algorithm):
    def __init__(self, dimensions: list[float, float]):
        self.__dimensions = dimensions

    def process(self, image: Image) -> Image:
        # TODO: implement zoom
        return image
