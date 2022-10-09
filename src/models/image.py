import numpy as np


class Image:
    def __init__(
        self,
        image: np.array,
        path: str,
    ):
        self.image = image
        self.path = path
