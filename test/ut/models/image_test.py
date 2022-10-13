import numpy as np
import cv2
from unittest import TestCase

from src.models.image import Image

DUMMY_PATH = "test/data/pig.jpg"
DUMMY_IMAGE = cv2.imread(DUMMY_PATH, cv2.IMREAD_COLOR)


class ImageTest(TestCase):
    def test_create_image(self):
        image = Image(DUMMY_IMAGE, DUMMY_PATH)
        assert np.array_equal(image.image, DUMMY_IMAGE)
        assert image.path == DUMMY_PATH

    def test_get_name(self):
        image = Image(DUMMY_IMAGE, DUMMY_PATH)
        assert image.get_name() == "pig.jpg"
