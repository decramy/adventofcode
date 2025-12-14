#!/bin/env/python3
import re

with open("day4.txt") as file:
  for line in file:
    line = line.rstrip() 

    r = re.search(r"(\d+)-(\d+),(\d+)-(\d+)",line)
    g1 = list(range(int(r.group(1)),int(r.group(2))+1))
    g2 = list(range(int(r.group(3)),int(r.group(4))+1))

    # check if g1 covers g2
    if (min(g1) <= min(g2) and max(g1) >= max(g2)):
      print(line)
    
    # check if g2 covers g1 
    elif (min(g2) <= min(g1) and max(g2) >= max(g1)):
      print(line)
