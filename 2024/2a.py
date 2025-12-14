#!/bin/env/python3
from copy import copy 


safe = 0
with open("day2.txt") as file:
  for line in file:
    line = line.rstrip()
    x1 = line.split(" ")
    x = list(map(int, x1))

    unsafe = False
    print(x)

    
    # test if difference is too big
    last = x[0]
    for report in x[1:]:
      diff = abs(int(last)-int(report)) 
      print(diff, end=' ')
      if diff == 0 or diff > 3:
        unsafe = True

      last = report
    print(": ","Safe" if unsafe == False else "Unsafe")
    

    # test if all values are increasing/decreasing
    asc = copy(x)
    asc.sort()
    
    desc = copy(x)
    desc.sort(reverse=True)

    if x == asc:
      print("all ASC:", asc)
    elif x == desc:
      print("all DESC", desc)
    else:
      print("mixed x", x)
      print("mixed a", asc)
      print("mixed d", desc)
      unsafe = True

    if unsafe == False:
      safe = safe + 1
    print("--------")
print("safe:",safe)
