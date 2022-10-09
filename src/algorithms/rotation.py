from algorithm import Algorithm
from models.image import Image


class Rotation(Algorithm):
    def __init__(self, degrees: float):
        self.__degrees = degrees

    def process(image: Image) -> Image:
        # TODO: implement rotation
        return image
