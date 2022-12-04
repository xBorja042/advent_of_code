import os

file = os.path.join(os.getcwd(), "input_files", "input_04.txt")

with open(file) as f:
    lines = f.readlines()

l_sections = [element.replace("\n", "") for element in lines]

#l_sections = ["2-4,6-8",
#"2-3,4-5",
#"5-7,7-9",
#"2-8,3-7",
#"6-6,4-6",
#"2-6,4-8"]

def make_interval(d_sec:str) -> list:
    d_sec = d_sec.split("-")
    d_sec_l, d_sec_r = int(d_sec[0]), int(d_sec[1])
    if d_sec_l == d_sec_r:
        sec_list = [d_sec_l]
    else:
        sec_list = [section for section in range(d_sec_l, d_sec_r + 1)]
    return sec_list

total_pairs = 0
for section in l_sections:
    dw1, dw2 = section.split(",")[0], section.split(",")[1]
    l1, l2 = make_interval(dw1), make_interval(dw2)
    section_cont = list()
    s1,s2 = all(elem in l2 for elem in l1), all(elem in l1 for elem in l2)
    if s1 == True or s2 == True:
        total_pairs += 1 
        
print(f"Solution to day 4 part 1 is : {total_pairs}")


total_overlaps = 0
for section in l_sections:
    dw1, dw2 = section.split(",")[0], section.split(",")[1]
    l1, l2 = make_interval(dw1), make_interval(dw2)
    s1,s2 = any(item for item in l1 if item in l2), any(item for item in l2 if item in l1)
    if s1 == True or s2 == True:
        total_overlaps += 1 

print(f"Solution to day 4 part 2 is : {total_overlaps}")
    
        
            
    