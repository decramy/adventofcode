#!/bin/env/python3

# Corrected version using `pos` and explicit "first" logic for crossings.
# Defaults to example file `day1e.txt` (you can pass a filename as first arg).

import sys

pos = 50
c = 0

fname = sys.argv[1] if len(sys.argv) > 1 else "day1e.txt"

with open(fname) as file:
  for raw in file:
    line = raw.strip()
    if not line:
      continue

    direction = line[0]
    number = int(line[1:])

    print("pos: %i, line: %s, c: %i" % (pos, line, c))

    if direction == "L":
      # Steps from current pos needed to reach 0 when moving left
      first = pos if pos != 0 else 100
      if number >= first:
        c += 1 + (number - first) // 100
        print("calculated new c: %i" % c)

      pos = (pos - number) % 100
      print("pos after move: %i" % pos)

    elif direction == "R":
      # Steps from current pos needed to reach 0 when moving right
      first = (100 - pos) % 100
      if first == 0:
        first = 100
      if number >= first:
        c += 1 + (number - first) // 100
        print("calculated new c: %i" % c)

      pos = (pos + number) % 100
      print("pos after move: %i" % pos)

    else:
      print("%s not L or R" % line)

    print("###############################")

print(c)
