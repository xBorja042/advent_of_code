import os
import pandas as pd
# print(os.getcwd())
# print(os.listdir(os.path.join(os.getcwd(), "input_files")))


file = os.path.join(os.getcwd(), "input_files", "input_01.txt")

with open(file) as f:
    lines = f.readlines()
    
n_lines = [(element.replace("\n", "")) for element in lines]

element_split = list()

for index, element  in enumerate(n_lines):
    # print(element, index)
    if element == "":
        element_split.append(index)
        # print("ENTRA")
        
df = pd.DataFrame({"a": n_lines})
# df = df[~df.index.isin(element_split)]

l_calories = list()
split_0 = 0
for split in element_split:
    # print(df.iloc[split_0:split])
    calories_dwarf = df.iloc[split_0:split].astype(int).sum().values[0]
    l_calories.append(calories_dwarf)
    split_0 = split+1
    # print("otro")
    
max_dwarf = pd.Series(l_calories).max()

print(f"Solution for first part is {max_dwarf}")

three_elves_sum = pd.Series(l_calories).sort_values(ascending=False).head(3).sum()
print(f"Solution for second part is {three_elves_sum}")