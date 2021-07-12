from abc import ABC, abstractmethod


class ActionProcessor(ABC):
    def __init__(self, automation_processor, variables):
        self.automation_processor = automation_processor
        self.variables = variables

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process(self):
        pass
