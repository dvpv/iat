from algorithm import Algorithm
from models.image import Image


class Crop(Algorithm):
    def __init__(self, dimensions: list[float, float]):
        self.__dimensions = dimensions

    def process(image: Image) -> Image:
        # TODO: implement crop
        return image
