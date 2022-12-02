import os
import pandas as pd
# print(os.getcwd())
# print(os.listdir(os.path.join(os.getcwd(), "input_files")))


file = os.path.join(os.getcwd(), "input_files", "input_02.txt")

with open(file) as f:
    lines = f.readlines()

# lines = ['A Y',
# 'B X',
# 'C Z']

games = [(element.replace("\n", "").replace(" ", "")).lower() for element in lines]

def compute_shape(sc):
    shape = 0
    if sc[1] == "x":
        shape = 1
    elif sc[1] == "y":
        shape = 2
    elif sc[1] == "z":
        shape = 3 
    return shape

def compute_outcome(sc):
    outcome = 0
    if sc[0] == "a" and sc[1] == "x" or sc[0] == "b" and sc[1] == "y" or sc[0] == "c" and sc[1] == "z":
        outcome += 3
    elif sc[0] == "a" and sc[1] == "y" or sc[0] == "b" and sc[1] == "z" or sc[0] == "c" and sc[1] == "x":
        outcome += 6
    else:
        outcome = 0
    return outcome

total_sc = sum([compute_outcome(game) + compute_shape(game) for game in games])

print(f" Solution to first part: {total_sc}")

def fix_games(game):
    fixed_game = game[0]
    if game[1] == "y":
        if game[0] == "a":
           fixed_game += "x"
        elif game[0] == "b":
              fixed_game += "y"
        elif game[0] == "c":
              fixed_game += "z"
    elif game[1] == "x":
        if game[0] == "a":
           fixed_game += "z"
        elif game[0] == "b":
              fixed_game += "x"
        elif game[0] == "c":
              fixed_game += "y"
    else:
        if game[0] == "a":
           fixed_game += "y"
        elif game[0] == "b":
              fixed_game += "z"
        elif game[0] == "c":
              fixed_game += "x"
    return fixed_game


fixed_games = [fix_games(game) for game in games]


fixed_total_sc = sum([compute_outcome(game) + compute_shape(game) for game in fixed_games])

print(f" Solution to second part: {fixed_total_sc}")













