from .action import ActionProcessor
from automation.utils import get_till_available


class CompareActionProcessor(ActionProcessor):
    __COMMAND__ = "COMPARE"

    def validate(self):
        return True, None

    def process(self):
        query = []
        comment = ''
        for each in self.variables:
            if each.lower().startswith("comment:"):
                comment = each.replace("COMMENT:", '')
                continue
            if each.lower().startswith("cond:"):
                query.append(each.replace('COND:', ''))
            else:
                query.append(f'"{each}"')
        query = ''.join(query)
        query_output = eval(query)
        print(f"\t\tQuery: {query}")
        print(f"\t\tResult: {query_output}")
        self.automation_processor.results.append([self.block_name, comment, query, query_output])
