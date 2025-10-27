import sys, os
path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(os.path.abspath(path))

from utils.utils import load_input_data

file = load_input_data(filename=f"day_2\input_file.txt")
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "input_file.txt")

with open(input_file, "r", encoding="utf-8") as f:
    total_reports = list()
    for reports in f:
        total_reports.append(reports.replace("\n","").split(" "))
    
print(total_reports)
