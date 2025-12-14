#!/bin/env/python3

load = []
cals = 0

with open("day1.txt") as file:
  for line in file:
    if line.rstrip() != "":
      cals = cals + int(line)
    else:
      load.append(cals)
      cals = 0

print("size:", len(load))
print("highest:",max(load))

s = sorted(load,reverse=True)
print("sum top 3:", s[0]+s[1]+s[2])

