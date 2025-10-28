import sys, os
import numpy as np

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.abspath(path))

from utils.utils import load_input_data

file = load_input_data(filename=f"day_2\input_file.txt")
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "input_file.txt")

total_reports = 0
with open(input_file, "r", encoding="utf-8") as f:
    # total_reports = list()
    for reports in f:
        report = np.array([int(e) for e in reports.replace("\n","").split(" ")])
        if all(np.sort(report) == report) or all(np.sort(report)[::-1] == report):
            diff_report = abs(np.diff(report))
            print(report, "Sorted", diff_report)
            final_check = (~np.isin(diff_report, [1, 2, 3])).any()
            if not final_check:
                total_reports+=1
                print(report, "Sorted and valid")
            else:
                print(report, "Sorted but not valid")
        else:
            print(report, "Not sorted")
        # total_reports.append(report)
    
print(f"Solution to task 1 day 2 ---> {total_reports}")
