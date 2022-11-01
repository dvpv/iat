from typing import List

import cv2
from src.models.image import Image
from src.operations.operation import Operation
from src.utils.parsers import append_to_image_name, parse_operation
from src.utils.extractors import extract_key


chain_index = 1


class Chain:
    def from_dict(d: dict):
        global chain_index
        name = extract_key(
            "name",
            d,
            [str],
            optional=True,
            default_value=str(chain_index),
        )
        if name == str(chain_index):
            chain_index = chain_index + 1
        save_each_step = extract_key(
            "name",
            d,
            [str],
            optional=True,
            default_value=False,
        )
        encoded_operations = extract_key("operations", d, [list])
        operations: List[Operation] = []
        for encoded in encoded_operations:
            operations.append(parse_operation(encoded))
        operations[-1].save_result = True  # Save the result for the last operation
        return Chain(
            name=name,
            operations=operations,
            save_each_step=save_each_step,
        )

    def __init__(self, name: str, operations: List[Operation], save_each_step: bool):
        self.__name = name
        self.__operations = operations
        self.__save_each_step = save_each_step

    def process(self, image: Image, output_dir: str) -> None:
        for i, operation in enumerate(self.__operations):
            image = operation.process(image)
            if operation.save_result or self.__save_each_step:
                self.__export_image(image, i + 1, output_dir, operation.TYPE)

    def __export_image(
        self,
        image: Image,
        step: int,
        output_dir: str,
        operation_type: str = "",
    ) -> None:
        image_name = append_to_image_name(image.get_name(), f"_{self.__name}_{step}")
        print(
            f"        saving image at {output_dir}/{image_name} after {operation_type}"
        )
        cv2.imwrite(f"{output_dir}/{image_name}", image.image)

    def get_name(self) -> str:
        return self.__name
