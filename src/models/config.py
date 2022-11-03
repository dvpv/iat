from copy import deepcopy
from typing import List
from src.operations.macro import Macro
from src.models.image import Image
from src.models.chain import Chain
from src.utils.extractors import extract_key

OUTPUT_DIR_CONFIG_KEY: str = "outputDir"


class Config:
    def from_dict(d: dict):
        encoded_macros = extract_key("macros", d, [dict])
        macros: List[Macro] = []
        for key in encoded_macros:
            macros.append(Macro.from_dict(encoded_macros[key], key, macros))
        encoded_chains = extract_key("chains", d, [list])
        chains = [Chain.from_dict(encoded, macros) for encoded in encoded_chains]
        return Config(chains=chains, macros=macros)

    def __init__(self, chains: List[Chain], macros: List[Chain]):
        self.__chains = chains
        self.__macros = macros

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
