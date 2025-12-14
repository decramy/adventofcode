#!/bin/env/python3

left = []
right = []
with open("day1.txt") as file:
  for line in file:
    line = line.rstrip()
    x = line.split("   ")

    left.append(int(x[0]))
    right.append(int(x[1]))

left.sort()
right.sort()

score = 0

for index,item in enumerate(left):
  print(index,index)

  print("i:",left[index], right[index])
  diff = abs(left[index] - right[index])
  print("d:",diff)
  score = score + diff

print(score)
