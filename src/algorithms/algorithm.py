from abc import ABC, abstractmethod

from models.image import Image


class Algorithm(ABC):
    @abstractmethod
    def process(image: Image) -> Image:
        pass
