#!/bin/env/python3
import json

section1 = []
section2 = []
section = 1

with open("day5.txt") as file:
  for line in file:
    line = line.rstrip()
    if line == "":
      section = 2
    elif section == 1:
      section1.append(line)
    elif section == 2:
      section2.append(line)

after = {}
notbefore = {}
for item in section1:
  key,value = item.split("|")
  key = int(key)
  value = int(value)

  if key in after:
    after[key].append(value)
  else:
    after[key] = [value]

  if value in notbefore:
    notbefore[value].append(key)
  else:
    notbefore[value] = [key]

print(json.dumps(after,sort_keys=True, indent=4))
print(json.dumps(notbefore,sort_keys=True,indent=4))

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 4]
# 
# print(all(i in a for i in b)) # Checks if all items are in the list
# print(any(i in a for i in b)) # Checks if any item is in the list
good = []
for manual in section2:
  notgood = False
  pages = manual.split(",")
  pages = list(map(int,pages))
  print("pages:",pages)
  #reverse = list(reversed(pages))
  #print("reversed:",reverse)


  for index,page in enumerate(pages):
    if page not in after:
      print(page,"not found as key in 'after'")
    else:  
      hay = after[page]
      hay.sort()
      needle = pages[index+1:]
      needle.sort()
      print("After: checking for page",page,":",needle,"is in",hay)
      if not all(i in hay for i in needle):
        notgood = True
        print("After: Not Good...")
        break
      else:
        print("After: Seems to be good")

    if page not in notbefore:
      print(page,"not found as key in 'notbefore'")
    else:
      hay = notbefore[page]
      hay.sort()
      needle = pages[index+1:]
      needle.sort()

      print("NotBefore: checking for page",page,":",needle,"is not in",hay)
      if not all(i not in hay for i in needle):
        notgood = True
        print("NotBefore: Not Good...")
        break
      else:
        print("NotBefore: Seems to be good")
  
  if notgood == False:
    print("score plus 1!")
    good.append(manual)


score=0
for go in good:
  go = go.split(",")
  print("go",go)
  middle = int((len(go) - 1)/2)
  score += int(go[middle])

print("score:",score)
