from typing import List
from webbrowser import Opera

from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class Crop(Operation):
    TYPE = "crop"

    def from_dict(d: dict) -> Operation:
        return Crop(
            dsize=[extract_key("x", d, [int]), extract_key("y", d, [int])],
            save_result=extract_save(d),
        )

    def __init__(self, dsize: List[int], save_result: bool = False):
        self.__dsize = dsize
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        shape = image.image.shape
        assert self.__dsize[0] <= shape[0], f"{self.__dsize[0]} <= {shape[0]}"
        assert self.__dsize[1] <= shape[1], f"{self.__dsize[0]} <= {shape[0]}"
        image.image = image.image[
            int(shape[0] / 2 - self.__dsize[0] / 2) : int(
                shape[0] / 2 + self.__dsize[0] / 2
            ),
            int(shape[1] / 2 - self.__dsize[1] / 2) : int(
                shape[1] / 2 + self.__dsize[1] / 2
            ),
        ]
        return image
