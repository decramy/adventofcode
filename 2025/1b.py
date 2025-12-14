#!/bin/env/python3

xold = 50
xnew = 0
c = 0

with open("day1e.txt") as file:
  for line in file:
    direction = line[:1]
    number = int(line[1:])

    print("xold: %i, line: %s, c: %i" % (xold,line[:-1],c))
    if direction == "L":
      xnew = xold - number
      print("xnew: %i" % xnew) 

      if xnew <= 0 and xold >0:
        c = c + (xnew // -100) + 1
        print("calculated new c: %i" % c) 

    elif direction == "R":
      xnew = xold + number
      print("xnew: %i" % xnew)

      if xnew >= 100:
        c = c + (xnew // 100)
        print("calculated new c: %i" % c)

    else:
      print("%s not L or R" % line)

#    if xnew == 0:
#      c = c + 1
#      print("xnew: 0, so c++")

    xold = xnew % 100
    print("###############################")

print(c)
