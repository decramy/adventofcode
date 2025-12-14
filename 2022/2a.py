#!/bin/env/python3

# A X Rock
# B Y Paper
# C Z Scissor


score = 0

with open("day2.txt") as file:
  for line in file:
    line = line.rstrip()
    he,me = line.split(" ")

    if me == "X":
        score = score + 1   # Omdat ik rock gebruik
        if he == "A":
          score = score + 3 
        if he == "B":
          score = score + 0 
        if he == "C":
          score = score + 6 
    elif me == "Y":
        score = score + 2   # Omdat ik paper gebruik
        if he == "A": 
          score = score + 6 
        if he == "B":
          score = score + 3 
        if he == "C":
          score = score + 0 
    elif me == "Z":
        score = score + 3   # Omdat ik scissor gebruik
        if he == "A":
          score = score + 0 
        if he == "B":
          score = score + 6 
        if he == "C":
          score = score + 3 
    else:
        print("should not be happening")

print (score) 
