#!/bin/env/python3

left = []
right = []
with open("day1.txt") as file:
  for line in file:
    line = line.rstrip()
    x = line.split("   ")

    left.append(int(x[0]))
    right.append(int(x[1]))

score = 0

for item in left:
  amount = right.count(item)
  distance = item * amount
  score = score + distance


print(score)
