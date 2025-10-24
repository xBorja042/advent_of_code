import os 

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "input_file.txt")

with open(input_file, "r", encoding="utf-8") as f:
    locs_1, locs_2 = [], []
    for locations in f:
        locs = locations.rstrip().split("   ")
        locs_1.append(int(locs[0]))
        locs_2.append(int(locs[1]))

print(locs_1, locs_2)
        
        