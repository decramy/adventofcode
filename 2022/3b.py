#!/bin/env/python3


score = 0
frop = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

runner = 0
group = []
total = []

with open("day3.txt") as file:
  for line in file:
    line = line.rstrip()
    
    group.append(line)
    if runner != 2:
      runner = runner + 1
    else:
      total.append(group)
      group = []
      runner = 0

for group in total:
  for char in group[0]:
    if char in group[1] and char in group[2]:
      every = char
  print(every, group)
  score = score + frop.find(every) + 1

print(score)
