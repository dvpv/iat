import cv2
import numpy as np
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save


class GammaCorrection(Operation):
    TYPE = "gammaCorrection"

    def from_dict(d: dict) -> Operation:
        return GammaCorrection(
            gamma=extract_key("gamma", d, [float]),
            save_result=extract_save(d),
        )

    def __init__(self, gamma: float, save_result: bool = False):
        self.__gamma = gamma
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        inv_gamma = 1.0 / self.__gamma
        table = np.array(
            [((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)],
        ).astype("uint8")

        image.image = cv2.LUT(image.image, table)

        return image
