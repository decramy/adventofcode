#!/bin/env/python3

x = 50
c = 0

with open("day1.txt") as file:
  for line in file:
    direction = line[:1]
    number = int(line[1:])

    print("x: %i, line: %s" % (x,line))
    if direction == "L":
      x = x - number
    elif direction == "R":
      x = x + number
    else:
      print("%s not L or R" % line)

    print("x: %i" % x)

    while x < 0:
      x = 100 + x
      print("x: %i, fixed by +100" % x)

    while x >= 100:
      x = x - 100
      print("x: %i, fixed by -100" % x)
  
    if x == 0:
      c = c + 1

print(c)
