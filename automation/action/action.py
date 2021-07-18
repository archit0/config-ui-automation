from abc import ABC, abstractmethod


class ActionProcessor(ABC):
    def __init__(self, automation_processor, variables, block_name):
        self.automation_processor = automation_processor
        self.variables = variables
        self.block_name = block_name

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process(self):
        pass
