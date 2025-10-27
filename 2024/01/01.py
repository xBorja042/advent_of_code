import os 
import numpy as np
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "input_file.txt")

with open(input_file, "r", encoding="utf-8") as f:
    locs_1, locs_2 = [], []
    for locations in f:
        locs = locations.rstrip().split("   ")
        locs_1.append(int(locs[0]))
        locs_2.append(int(locs[1]))


locs_1_, locs_2_ = np.sort(np.array(locs_1)), np.sort(np.array(locs_2))
print(locs_1_, locs_2_)
print(f"Solution to first part challenge day 1 ---> {np.sum(abs(locs_1_-locs_2_))}")

locs_1, locs_2 = np.array(locs_1), np.array(locs_2)