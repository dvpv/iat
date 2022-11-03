from src.models.chain import Chain
from src.operations.operation import Operation
from src.models.image import Image


class Macro(Operation):
    def from_dict(d: dict, name: str, macros) -> Operation:
        chain = Chain.from_dict(d, macros)
        return Macro(
            name=name,
            chain=chain,
        )

    def __init__(
        self,
        name: str,
        chain: Chain,
    ):
        self.TYPE = name
        self.__chain = chain

    def process(self, image: Image) -> Image:
        return self.__chain.process(image)
