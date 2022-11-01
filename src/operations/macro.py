from src.models.chain import Chain
from src.operations.operation import Operation
from src.models.image import Image


class Macro(Operation):
    def from_dict(d: dict, name: str, output_dir: str) -> Operation:
        chain = Chain.from_dict(d)
        chain.export_images = False
        return Macro(
            name=name,
            chain=chain,
            output_dir=output_dir,
        )

    def __init__(
        self,
        name: str,
        chain: Chain,
        output_dir: str,
        save_result: bool = False,
    ):
        self.TYPE = name
        self.__chain = chain
        self.__output_dir = output_dir
        self.save_result = save_result

    def process(self, image: Image) -> Image:
        print(self.__output_dir)
        return self.__chain.process(image, self.__output_dir)
