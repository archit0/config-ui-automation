from .action import ActionProcessor
from automation.utils import get_till_available


class TypeActionProcessor(ActionProcessor):
    __COMMAND__ = "TYPE"

    def validate(self):
        if not 2 <= len(self.variables) <= 3:
            return False, f"Parameters not match. Expected 2-3 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        value = self.variables[0]
        location = self.variables[1]
        if len(self.variables) == 3:
            location_type = self.variables[2].lower()
        else:
            location_type = 'xpath'

        func_name = f'find_element_by_{location_type}'
        get_till_available(self.automation_processor.driver, 10, func_name, location).send_keys(value)
