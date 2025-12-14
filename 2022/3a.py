#!/bin/env/python3


score = 0
frop = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

runner = 0
group = []
total = []

with open("day3.txt") as file:
  for line in file:
    line = line.rstrip()
    
    half = int( len(line) / 2 )
    c1 = line[:half]
    c2 = line[half:]

    for item in c1:
      if item in c2:
        both = item

    score = score + frop.find(both) + 1
print(score)
