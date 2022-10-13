from typing import List
from algorithms.algorithm import Algorithm


class Config:
    def __init__(self, operations: List[Algorithm], save_each_step):
        self.operations = operations
        self.save_each_step = save_each_step
