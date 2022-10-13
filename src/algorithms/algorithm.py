from abc import ABC, abstractmethod

from src.models.image import Image


class Algorithm(ABC):
    save_result: bool = False

    @abstractmethod
    def process(self, image: Image) -> Image:
        pass
