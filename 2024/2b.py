#!/bin/env/python3
from copy import copy 

def check(input):
  unsafe = False
  print(input)

  # test if all values are increasing/decreasing
  asc = copy(input)
  asc.sort()
  
  desc = copy(input)
  desc.sort(reverse=True)

  if input == asc:
    print("all ASC:", asc)
  elif input == desc:
    print("all DESC", desc)
  else:
    print("mixed input", input)
    print("mixed asc  ", asc)
    print("mixed desc ", desc)
    unsafe = "Mixed"

  
  # test if difference is too big
  last = input[0]
  for report in input[1:]:
    diff = abs(int(last)-int(report)) 
    print(diff, end=' ')
    if diff == 0 or diff > 3:
      unsafe = "Too different"

    last = report
  print(": ","Safe" if unsafe == False else "Unsafe")

  return unsafe
 


# All we are looking for is if it is possible to create a safe sequence by removing any of the elements. 
# If we remove either 3 or 2 it becomes safe therefore it’s safe overall. It does not care which element you remove to make it safe

# ofwel: als ie unsafe is, haal dan even een item weg en test of ie dan wel safe wordt.


safe = 0
with open("day2.txt") as file:
  for line in file:
    line = line.rstrip()
    x1 = line.split(" ")
    x = list(map(int, x1))

    unsafe = check(x)
    
    if unsafe == False:
      print("it was considered safe")
      safe = safe + 1
    else:
      for index,value in enumerate(x):
        test = copy(x)
        test.pop(index)
        unsafe = check(test)
        if unsafe == False:
          safe = safe + 1
          break
        print("---")
    print("---------------")
print("safe:",safe)
