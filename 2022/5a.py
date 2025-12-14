#!/bin/env/python3
import re


input = """
                [B]     [L]     [S]
        [Q] [J] [C]     [W]     [F]
    [F] [T] [B] [D]     [P]     [P]
    [S] [J] [Z] [T]     [B] [C] [H]
    [L] [H] [H] [Z] [G] [Z] [G] [R]
[R] [H] [D] [R] [F] [C] [V] [Q] [T]
[C] [J] [M] [G] [P] [H] [N] [J] [D]
[H] [B] [R] [S] [R] [T] [S] [R] [L]
 1   2   3   4   5   6   7   8   9 
"""
data = {
 1: ["R","C","H"],
 2: ["F","S","L","H","J","B"],
 3: ["Q","T","J","H","D","M","R"],
 4: ["J","B","Z","H","R","G","S"],
 5: ["B","C","D","T","Z","F","P","R"],
 6: ["G","H","C","T"],
 7: ["L","W","P","B","Z","V","N","S"],
 8: ["C","G","Q","J","R"],
 9: ["S","F","P","H","R","T","D","L"]
}
 

def print_data(data):
  print("----DATA-------------------------------------")
  for key,value in data.items():
    print("{} ({}): {}".format(key,len(value),value))
  print("----/DATA------------------------------------")


pattern = r"move (\d+) from (\d) to (\d)"

with open("day5.txt") as file:
  for line in file:
    line = line.rstrip()
    
    result = re.search(pattern,line)
    num = int(result.group(1))
    source = int(result.group(2))
    dest = int(result.group(3))


    print_data(data)
    print(line)
    print("old row ",source,":",data[source])
    cut = data[source][:num]
    print("cut from",source,":",cut)
    data[source] = data[source][num:]
    print("new row ",source,":",data[source])
    print("---")
    print("old dest",dest,":",data[dest])
    data[dest] = list(reversed(cut)) + data[dest] # paste
    print("new dest",dest,":",data[dest])

for key,value in data.items():
  print(value[0], end='')
print()
