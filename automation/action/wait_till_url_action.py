from .action import ActionProcessor
from automation.utils import wait_till_this_url


class WaitForUrlProcessor(ActionProcessor):
    __COMMAND__ = "WAIT_TILL_URL"

    def validate(self):
        if not 2 <= len(self.variables):
            return False, f"Parameters not match. Expected 2 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        time = self.variables[0]
        url = self.variables[1]
        wait_till_this_url(self.automation_processor.driver, url, time)
