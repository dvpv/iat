from operations.operation import Operation
from src.models.image import Image


class Crop(Operation):
    def __init__(self, dimensions: list[float, float], save_result: bool):
        self.__dimensions = dimensions
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        # TODO: implement crop
        return image
