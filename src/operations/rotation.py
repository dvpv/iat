import cv2
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save

ROTATION_MAP = {90: 0, 180: 1, 270: 2}


class Rotation(Operation):
    TYPE = "rotation"

    def from_dict(d: dict) -> Operation:
        degrees = extract_key("degrees", d, [int])
        if degrees not in ROTATION_MAP:
            raise Exception("Rotation needs to be either 90, 180 or 270 degrees")
        rotation = ROTATION_MAP[degrees]
        return Rotation(
            rotation,
            save_result=extract_save(d),
        )

    def __init__(self, rotation: int, save_result: bool):
        self.__rotation = rotation
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.rotate(image.image, self.__rotation)
        return image
