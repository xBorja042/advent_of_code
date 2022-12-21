# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:20:15 2022

@author: bgonzalez
"""

lines = [[1,1,3,1,1],
[1,1,5,1,1],

[[1],[2,3,4]],
[[1],4],

[9],
[[8,7,6]],

[[4,4],4,4],
[[4,4],4,4,4],

[7,7,7,7],
[7,7,7],

[],
[3],

[[[]]],
[[]],

[1,[2,[3,[4,[5,6,7]]]],8,9],
[1,[2,[3,[4,[5,6,0]]]],8,9]]

def parse_lines(lista1, lista2):
    for subl1 in lista1:
        for subl2 in lista2:
            if len(subl1) == len(subl2):
                for index, e1 in enumerate(lista1):
                    e2 = lista2[index]
                    print(e1, e2)
                    if e1 < e2:
                        print("Menor")

for i in range(len(lines[:1])):
    l0, l1 = lines[i], lines[i+1]
    parse_lines(l0, l1)