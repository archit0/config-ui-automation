from .action import ActionProcessor
from automation.utils import get_till_available


class ClickActionProcessor(ActionProcessor):
    __COMMAND__ = "CLICK"

    def validate(self):
        if not 1 <= len(self.variables) <= 2:
            return False, f"Parameters not match. Expected 1-2 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        location = self.variables[0]
        if len(self.variables) == 2:
            location_type = self.variables[1].lower()
        else:
            location_type = 'xpath'

        func_name = f'find_element_by_{location_type}'
        get_till_available(self.automation_processor.driver, 10, func_name, location).click()
