with open("input_file.txt", "r", encoding="utf-8") as f:
    locs_1, locs_2 = [], []
    for locations in f:
        locs = locations.rstrip().split("   ")
        locs_1.append(int(locs[0]))
        locs_2.append(int(locs[1]))

print(locs_1, locs_2)
        
        