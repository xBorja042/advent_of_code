import os

file = os.path.join(os.getcwd(), "input_files", "input_03.txt")

with open(file) as f:
    lines = f.readlines()

l_items = [element.replace("\n", "") for element in lines]

#l_items = ["vJrwpWtwJgWrhcsFMMfFFhFp",
#"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#"PmmdzqPrVvPwwTWBwg",
#"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#"ttgJtRGJQctTZtZT",
#"CrZsJsPPZsGzwwsLwLmpwMDw"]

l_intersect = list()

for item in l_items:
    s2 = int(len(item)/2)
    p1, p2 = item[:s2], item[s2:]
    l_intersect.append([item1 for item1 in p1 if item1 in p2][0])
    
def compute_value(l:str) -> int:
    value = 0
    if l.islower():
        value = ord(l) - 96
    else:
        value = ord(l) - 64 + 26
    return value

priorities = sum([compute_value(letter) for letter in l_intersect])

print(f" Solution to day 3 part 1 is: {priorities}")

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


l_badges = list()
for group in chunker(l_items, 3):
    set1, set2, set3 = set(group[0]), set(group[1]), set(group[2])
    badge = "".join(set(set1).intersection(set(set2), set(set3)))
    l_badges.append(badge)
    
total_badges = sum([compute_value(badge) for badge in l_badges])

print(f" Solution to day 3 part 2 is: {total_badges}")
    



    


