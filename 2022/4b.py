#!/bin/env/python3
import re

with open("day4.txt") as file:
  for line in file:
    line = line.rstrip() 

    r = re.search(r"(\d+)-(\d+),(\d+)-(\d+)",line)
    g1 = list(range(int(r.group(1)),int(r.group(2))+1))
    g2 = list(range(int(r.group(3)),int(r.group(4))+1))


    # 2-4,6-8
    # 5-7,7-9
    # 6-8,2-4

    if (max(g1) >= min(g2)):      # de max van g1 overlapt met de min van g2
      if not min(g1) > max(g2):   # maar g1 zit niet helemaal rechts van g2
        print(line)
