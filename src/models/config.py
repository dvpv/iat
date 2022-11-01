from copy import deepcopy
from typing import List
from src.models.image import Image
from src.models.chain import Chain
from src.utils.extractors import extract_key


class Config:
    def from_dict(d: dict):
        encoded_chains = extract_key("chains", d, [list])
        chains: List[Chain] = []
        for encoded in encoded_chains:
            chains.append(Chain.from_dict(encoded))
        return Config(
            chains=chains,
        )

    def __init__(self, chains: List[Chain]):
        self.__chains = chains

    def process_image(self, image: Image, output_dir: str) -> None:
        for chain in self.__chains:
            print(f"    running chain {chain.get_name()}")
            chain.process(
                # deepcopy so the image can be processed by multiple chains
                deepcopy(image),
                output_dir,
            )

    def process_images(self, images: List[Image], output_dir: str) -> None:
        for image in images:
            print(f"processing {image.path}")
            self.process_image(image, output_dir)
