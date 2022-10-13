import numpy as np


class Image:
    def __init__(
        self,
        image: np.array,
        path: str,
    ):
        self.image = image
        self.path = path

    def get_name(self) -> str:
        return self.path.split("/")[-1].split("\\")[-1]
