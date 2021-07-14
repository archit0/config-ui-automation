import time
from .action import ActionProcessor


class WaitProcessor(ActionProcessor):
    __COMMAND__ = "WAIT"

    def validate(self):
        if not 1 <= len(self.variables):
            return False, f"Parameters not match. Expected 1 Parameters. Got {len(self.variables)}"
        return True, None

    def process(self):
        time_to_wait = self.variables[0]
        time.sleep(time_to_wait)
