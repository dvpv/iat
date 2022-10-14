from typing import List
import cv2
from src.models.config import Config
from src.operations.operation import Operation
from src.models.image import Image
from src.utils.parsers import append_to_image_name


def export(image: Image, step: int, output_dir: str) -> None:
    image_name = append_to_image_name(image.get_name(), f"_{step}")
    print(f"saving image at {output_dir}/{image_name}")
    cv2.imwrite(f"{output_dir}/{image_name}", image.image)


def process(
    image: Image,
    config: Config,
    output_dir: str,
) -> None:
    i = 0
    for i, operation in enumerate(config.operations):
        image = operation.process(image)
        if operation.save_result or config.save_each_step:
            export(image, i + 1, output_dir)


def process_images(
    images: List[Image],
    config: Config,
    output_dir: str,
) -> None:
    for image in images:
        print(f"processing {image.path}")
        process(image, config, output_dir)
