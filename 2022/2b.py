#!/bin/env/python3

# A X Rock    1
# B Y Paper   2
# C Z Scissor 3

# X loose     0
# Y draw      3
# Z win       6

score = 0

with open("day2.txt") as file:
  for line in file:
    line = line.rstrip()
    he,me = line.split(" ")


    # score = score + <material> + <outcome>
    if he == "A":
        if me == "X":
	  # need to loose, so I need Scissor
          score = score + 3 + 0 
        if me == "Y":
	  # need draw, so I need Rock
          score = score + 1 + 3 
        if me == "Z":
	  # need win, so I need Paper
          score = score + 2 + 6 
    elif he == "B":
        if me == "X": 
          score = score + 1 + 0 
        if me == "Y":
          score = score + 2 + 3
        if me == "Z":
          score = score + 3 + 6
    elif he == "C":
        if me == "X":
          score = score + 2 + 0
        if me == "Y":
          score = score + 3 + 3
        if me == "Z":
          score = score + 1 + 6
    else:
        print("should not be happening")

print (score) 
