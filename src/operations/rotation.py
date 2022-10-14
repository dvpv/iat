from webbrowser import Opera
from src.operations.operation import Operation
from src.models.image import Image


class Rotation(Operation):
    def __init__(self, degrees: float, save_result: bool):
        self.__degrees = degrees
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        # TODO: implement rotation
        return image
