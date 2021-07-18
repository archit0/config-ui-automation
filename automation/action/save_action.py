from .action import ActionProcessor
from automation.utils import get_till_available


class SaveActionProcessor(ActionProcessor):
    __COMMAND__ = "SAVE_DATA"
    IGNORE_VARIABLE_REPLACEMENT = [0]

    def validate(self):
        if not 2 <= len(self.variables) <= 3:
            return False, f"Parameters not match. Expected 2-3 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        variable_name = self.variables[0]
        location = self.variables[1]
        if len(self.variables) == 3:
            location_type = self.variables[2].lower()
        else:
            location_type = 'xpath'

        func_name = f'find_element_by_{location_type}'
        data = get_till_available(self.automation_processor.driver, 10, func_name, location)
        if not data:
            print("\t\tData not Found")
        else:
            print(f"\t\tDATA: {data.text}")
            self.automation_processor.context[variable_name] = data.text
