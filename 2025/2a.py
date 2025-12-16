#!/bin/env/python3

c = 0

with open("day2.txt") as file:
  items = file.read().strip().split(",")
  for item in items:
    l,r = item.split("-")

    # ieder getal in de reeks
    r = range(int(l), int(r)+1)
    for i in r:
      i = str(i)
      # als de lengte van het getal deelbaar is         
      if len(i) % 2 == 0:
        # splits in twee helften     
        left,right = i[:len(i)//2], i[len(i)//2:] 
        
        # als de twee helften gelijk zijn
        if left == right:
          #print("found gelijk getal: %s" % i)
          c += int(i)                                  
    
print(c)
    
        
