#!/bin/env/python3
import re

score = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
with open("day3.txt") as file:
  for line in file:
    result = re.findall(pattern,line)
    for mul in result:
      score = score + (int(mul[0]) * int(mul[1]))

print(score)
