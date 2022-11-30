import os
import pandas as pd
# print(os.getcwd())
# print(os.listdir(os.path.join(os.getcwd(), "input_files")))


file = os.path.join(os.getcwd(), "input_files", "input1.txt")

with open(file) as f:
    lines = f.readlines()
    
n_lines = [int(element.replace("\n", "")) for element in lines]

times_growing = 0

for index, element in enumerate(n_lines):
    try:
        previous = n_lines[index-1]
        if element > previous:
            times_growing += 1
    except:
        print(f"Unable to compare {index}")
        
print(f"Solution part 1 ---> {times_growing}")

s = pd.DataFrame({"n":n_lines})
s["sum"] = s["n"].rolling(3).sum()
s["diff"] = s["sum"].diff()

solution = sum(s["diff"] > 0)

print(f"Solution to part 2 is ---> {solution}")