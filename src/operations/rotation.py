import cv2
from src.operations.operation import Operation
from src.models.image import Image


class Rotation(Operation):
    def __init__(self, degrees: float, save_result: bool):
        self.__degrees = degrees
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.rotate(image.image, self.__degrees)
        return image
