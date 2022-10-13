import cv2
from algorithms.algorithm import Algorithm

from models.image import Image
from utils.parsers import append_to_image_name


def export(image: Image, step: int, output_dir: str) -> None:
    image_name = append_to_image_name(image.get_name(), f"_{step}")
    cv2.imwrite(f"{output_dir}/{image_name}", image.image)


def process(
    image: Image,
    algorithms: list[Algorithm],
    output_dir: str,
) -> None:
    i = 0
    for i, algorithm in enumerate(algorithms):
        image = algorithm.process(image)
        if algorithm.save_result:
            export(image, i + 1, output_dir)
