#!/bin/env/python3
import re
import json

score = 0
skip = False
pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\)))"
with open("day3.txt") as file:
  for line in file:
    result = re.findall(pattern,line)
    for item in result:
      print(item)
      if item[0][0:3] == "mul" and skip == False:
        score = score + (int(item[1]) * int(item[2]))
        #print("adding...") 
      elif item[0] == "do()":
        skip = False
        #print("skip = False")
      elif item[0] == "don't()":
        skip = True
        #print("skip = True")



print(score)
