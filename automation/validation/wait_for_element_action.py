from .action import ActionProcessor
from automation.utils import get_till_available


class WaitForElementProcessor(ActionProcessor):
    __COMMAND__ = "WAIT_FOR_ELEMENT"

    def validate(self):
        if not 2 <= len(self.variables) <= 3:
            return False, f"Parameters not match. Expected 2-3 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        time = self.variables[0]
        location = self.variables[1]

        if len(self.variables) == 3:
            location_type = self.variables[2].lower()
        else:
            location_type = 'xpath'
        func_name = f'find_element_by_{location_type}'

        get_till_available(self.automation_processor.driver, time, func_name, location)
