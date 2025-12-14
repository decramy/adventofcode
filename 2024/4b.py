#!/bin/env/python3

data = []
with open("day4.txt") as file:
  for line in file:
    line = line.rstrip()
    row = []
    for char in line:
      row.append(str(char))
    data.append(row)


xmas = 0
rows = len(data)
for row,line in enumerate(data):
  cols = len(line)
  for col,char in enumerate(line):
    if char == "A" and row > 0 and row < rows -1 and col > 0 and col < cols -1:
      test = data[row-1][col-1] + data[row-1][col+1] + data[row+1][col-1] + data[row+1][col+1]

      if test == "MMSS" or test == "SSMM" or test == "MSMS" or test == "SMSM":
        xmas = xmas+1

print("XMAS:",xmas)
