from copy import deepcopy
from typing import List
from src.operations.macro import Macro
from src.models.image import Image
from src.models.chain import Chain
from src.utils.extractors import extract_key

OUTPUT_DIR_CONFIG_KEY: str = "outputDir"


class Config:
    def from_dict(d: dict, output_dir: str = None):
        output_dir = extract_key(
            OUTPUT_DIR_CONFIG_KEY,
            d,
            [str],
            optional=True,
            default_value=output_dir,
        )
        if output_dir == None:
            raise Exception("undefined output directory")
        encoded_macros = extract_key("macros", d, [dict])
        macros = [
            Macro.from_dict(encoded_macros[key], key, output_dir)
            for key in encoded_macros
        ]
        encoded_chains = extract_key("chains", d, [list])
        chains = [Chain.from_dict(encoded, macros) for encoded in encoded_chains]
        return Config(chains=chains, macros=macros, output_dir=output_dir)

    def __init__(self, chains: List[Chain], macros: List[Chain], output_dir: str):
        self.__chains = chains
        self.__macros = macros
        self.__output_dir = output_dir

    def process_image(self, image: Image, output_dir: str) -> None:
        for chain in self.__chains:
            print(f"    running chain {chain.get_name()}")
            chain.process(
                # deepcopy so the image can be processed by multiple chains
                deepcopy(image),
                output_dir,
            )

    def process_images(self, images: List[Image]) -> None:
        for image in images:
            print(f"processing {image.path}")
            self.process_image(image, self.__output_dir)
