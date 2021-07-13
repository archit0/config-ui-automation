import re
import time
from selenium import webdriver
from automation.action import ActionProcessor

ACTION_MAPPING = {}


def load_actions():
    subclasses = ActionProcessor.__subclasses__()
    for each_subclass in subclasses:
        ACTION_MAPPING[each_subclass.__COMMAND__.lower()] = each_subclass


load_actions()


class AutomationProcessor:
    def __init__(self, action_file, custom_object):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome()
        self.context = {}
        self.action_file = action_file
        self.custom_object = custom_object

    def extract_variables(self, command):
        variables = re.findall("\s\$(.*?)\$", command)
        # TODO Replace toggling off for certain action
        # If variable is actually a variable
        processed_variables = []
        for each in variables:
            if each in self.context:
                processed_variables.append(self.context[each])
            else:
                processed_variables.append(each)
        return processed_variables

    def group_blocks(self, lines):
        blocks = []
        for match in re.finditer("BLOCK\s{1,}START\s\$(.*)\$", lines, re.MULTILINE):
            block_name = match.group(1)
            end_block_line = lines.find("BLOCK END", match.end() + 1)
            commands = lines[match.end() + 1: end_block_line]
            blocks.append({"name": block_name, "commands": commands.strip().split("\n")})
        return blocks

    def process_block(self, name, block_commands):
        print(f"Processing: {name}")
        for each_line in block_commands:
            each_line = each_line.strip()
            if not each_line or each_line.startswith("#"):
                continue
            print(f"\t{each_line}")
            tokens = each_line.split(" ")
            command_start = tokens[0]
            command_class = ACTION_MAPPING.get(command_start.lower())
            if not command_class:
                raise Exception(f"Invalid command. {each_line}")
            variables = self.extract_variables(each_line)
            command_class_obj = command_class(self, variables)
            success, message = command_class_obj.validate()
            if not success:
                raise Exception(f"Command failed: [{each_line}]. Message: [{message}]")
            command_class_obj.process()

        print(f"Processing End")

    def process_action_file(self):
        lines = open(self.action_file).read()
        blocks = self.group_blocks(lines)
        for each_block in blocks:
            self.process_block(each_block['name'], each_block['commands'])


class AutomationDriverUtils:
    def __init__(self, automation_driver: AutomationProcessor):
        self.automation_driver = automation_driver

    def get_till_available(self, attribute, *args, **kwargs):
        for i in range(0, 10):
            try:
                ele = getattr(self.automation_driver.driver, attribute)(*args, **kwargs)
                if ele:
                    return ele
            except:
                pass
            print(f"\t\tTry {i + 1} failed {attribute} {args} {kwargs}")
            time.sleep(1)
        raise Exception(f"Element couldnt be find {attribute} {args} {kwargs}")

    def wait_till_this_url(self, url, times=10, sleep_sec=1):
        for i in range(0, times):
            if self.automation_driver.driver.current_url == url:
                return True
            time.sleep(sleep_sec)
        raise Exception("Didnt reach the url")


file = '../steps.cfg'

driver = AutomationProcessor(file, None)
driver.process_action_file()
