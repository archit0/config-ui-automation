from .action import ActionProcessor


class OpenActionProcessor(ActionProcessor):
    __COMMAND__ = "OPEN"

    def validate(self):
        if len(self.variables) != 1:
            return False, f"Parameters not match. Expected One Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        url = self.variables[0]
        self.automation_processor.driver.get(url)
