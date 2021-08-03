import os
import csv

from automation.processor import AutomationProcessor

# report_folder = input("Enter Folder Name(default=steps): ")
report_folder = "steps"
if not report_folder:
    report_folder = "steps"

output_folder = "results"
try:
    os.makedirs(output_folder)
except:
    pass

files = os.listdir(report_folder)
for each in files:
    file_path = f'{report_folder}/{each}'
    output_file_name = each.replace('.cfg', '.csv')
    with open(f'{output_folder}/{output_file_name}', 'w') as csv_file:
        output_file_path = csv.writer(csv_file)

        driver = AutomationProcessor(file_path, None)
        print("Processing file: {}", file_path)
        print("*" * 100)
        try:
            results = driver.process_action_file()
        except Exception as e:
            print("Exception occured", e)
        finally:
            output_file_path.writerow(['Block', 'Comment', 'Query', 'Output'])
            output_file_path.writerows(results)
            driver.driver.close()
