from typing import List
from src.operations.operation import Operation


class Config:
    def __init__(self, operations: List[Operation], save_each_step):
        self.operations = operations
        self.save_each_step = save_each_step
