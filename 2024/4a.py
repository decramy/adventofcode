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
test = ['X','M','A','S']

# horizontaal
h=0
for line in data:
  string = "".join(line)
  h = h + string.count("XMAS")
  print(string,"fwd:",h)
  h = h + string.count("SAMX")
  print(string,"rev:",h)
  print("---")
print("horizontaal",h)

# verticaal
v=0
for row,line in enumerate(data):
  for index,char in enumerate(line):
    if char == "X":
      try:
        four = [data[row][index],data[row+1][index],data[row+2][index],data[row+3][index]]
        if four == test:
          print("found a XMAS at index",index,"from row",row)
          v = v + 1
      except:
          xmas = xmas + 0
    if char == "S":
      try:
        four = [data[row+3][index],data[row+2][index],data[row+1][index],data[row][index]]
        if four == test:
          print("found a SAMX at index",index,"from row",row)
          v = v + 1
      except:
          xmas = xmas + 0
print("verticaal",v)

# diagonaal
# linksboven -> rechtsonder (en visaversa)
d=0
for row,line in enumerate(data):
  for index,char in enumerate(line):
    four = None
    if char == "X":
      try:
        four = [data[row][index],data[row+1][index+1],data[row+2][index+2],data[row+3][index+3]]
        if four == test:
          d = d + 1
          print("found diagonaal UL-BR from r,i",row,index,"till",row+3,index+3)
      except:
          xmas = xmas + 0
    if char == "S":
      try:
        four = [data[row+3][index+3],data[row+2][index+2],data[row+1][index+1],data[row][index]]
        if four == test:
          print("found diagonaal BR-UL till r,i",row,index,"from",row+3,index+3)
          d = d + 1
      except:
          xmas = xmas + 0
print("dia \\",d)


# rechtsboven -> linksonder
e=0
for row,line in enumerate(data):
  for index,char in enumerate(line):
    four = None
    if char == "X" and index>=3:
      try:
        four = [data[row][index],data[row+1][index-1],data[row+2][index-2],data[row+3][index-3]]
        if four == test:
          e = e + 1
          print("found diagonaal UR-BL from r,i",row,index,"till",row+3,index-3)
      except:
          xmas = xmas + 0
    if char == "S" and index>=3:
      try:
        four = [data[row+3][index-3],data[row+2][index-2],data[row+1][index-1],data[row][index]]
        if four == test:
          print("found diagonaal BL-UR till r,i",row,index,"from",row+3,index-3)
          e = e + 1
      except:
          xmas = xmas + 0
print("dia /",e)


xmas = h+v+d+e
print("XMAS:",xmas)
