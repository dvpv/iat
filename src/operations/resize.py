import cv2
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.extractors import extract_key, extract_save

INTER_MAP = {
    "area": cv2.INTER_AREA,
    "cubic": cv2.INTER_CUBIC,
    "lanczos4": cv2.INTER_LANCZOS4,
    "linear": cv2.INTER_LINEAR,
    "linear_exact": cv2.INTER_LINEAR_EXACT,
    "nearest": cv2.INTER_NEAREST,
}


class Resize(Operation):
    TYPE = "resize"

    def from_dict(d: dict) -> Operation:
        inter = extract_key("inter", d, [str], optional=True)
        inter = INTER_MAP[inter] if inter != None else cv2.INTER_NEAREST
        return Resize(
            height=extract_key("height", d, [int]),
            width=extract_key("width", d, [int]),
            inter=inter,
            save_result=extract_save(d),
        )

    def __init__(self, height: float, width: float, inter: int, save_result: bool):
        self.__height = height
        self.__width = width
        self.__inter = inter
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        image.image = cv2.resize(
            image.image,
            (self.__height, self.__width),
            interpolation=self.__inter,
        )
        return image
