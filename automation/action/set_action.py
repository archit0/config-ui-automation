from .action import ActionProcessor


class SetVariableActionProcessor(ActionProcessor):
    __COMMAND__ = "SET"
    IGNORE_VARIABLE_REPLACEMENT = [0]

    def validate(self):
        if len(self.variables) != 2:
            return False, f"Parameters not match. Expected Two Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        key = self.variables[0]
        value = self.variables[1]
        self.automation_processor.context[key] = value
