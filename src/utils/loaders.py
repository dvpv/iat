import os
from typing import List

import cv2
from src.models.image import Image
from src.utils.parsers import *

SUPPORTED_IMAGE_FORMATS = ["jpg", "jpeg"]


def load_images_from_dir(path: str) -> List[Image]:
    files = os.listdir(path)
    images = []
    for file in files:
        if get_file_type(file) in SUPPORTED_IMAGE_FORMATS:
            image_path = f"{path}/{file}"
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            images.append(Image(image, image_path))
    print(f"Loaded {len(images)} images")
    return images
