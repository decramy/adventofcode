#!/bin/env/python3

c = 0
ok = False

with open("day2.txt") as file:
  items = file.read().strip().split(",")
  for item in items:
    l,r = item.split("-")

    # ieder getal in de reeks
    r = range(int(l), int(r)+1)
    for i in r:
      i = str(i)
      
      # als de lengte van het getal deelbaar is         
      for delen in range(1,len(i)):
        #print("range: %s delen: %i" % (i,delen))
        # als de legte van het getal deelbaar is door het aantal delen
        if (len(i) % delen == 0):
          # splits in gelijke delen
          parts = []
          for p in range(0, len(i), delen):
            parts.append(i[p:p+delen])
          #print("  parts: %s" % parts)
          # als alle delen gelijk zijn
          if all(x == parts[0] for x in parts):
            print("  found gelijk getal: %s" % i)
            c += int(i)
            break # we hebben het getal al invalid gemaakt, dus stop met verder zoeken
                                        
    
print(c)
    
        
