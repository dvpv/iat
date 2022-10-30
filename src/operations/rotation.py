import cv2
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Rotation(Operation):
    TYPE = "rotation"

    def from_dict(d: dict) -> Operation:
        return Rotation(
            times=extract_key("times", d, [int]),
            save_result=extract_save(d),
        )

    def __init__(self, times: float, save_result: bool):
        self.__times = times
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.rotate(image.image, self.__times)
        return image
