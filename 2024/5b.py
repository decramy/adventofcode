#!/bin/env/python3
import json
from copy import copy

section1 = []
section2 = []
section = 1

with open("day5e.txt") as file:
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


def checkbad(data,pages):
  notgood = False
  after = data[0]
  notbefore = data[1]

  for index,page in enumerate(pages):
    if page not in after:
      print(page,"not found as key in 'after'")
      do = "Nothing"
    else:  
      hay = after[page]
      hay.sort()
      needle = pages[index+1:]
      needle.sort()
      print("After: checking for page",page,":",needle,"is in",hay)
      if not all(i in hay for i in needle):
        notgood = True
        print("After: Not Good...")
        return [index,pages]
        break
      else:
        print("After: Seems to be good")
        do = "Nothing"

    if page not in notbefore:
      print(page,"not found as key in 'notbefore'")
      do = "Nothing"
    else:
      hay = notbefore[page]
      hay.sort()
      needle = pages[index+1:]
      needle.sort()

      print("NotBefore: checking for page",page,":",needle,"is not in",hay)
      if not all(i not in hay for i in needle):
        notgood = True
        print("NotBefore: Not Good...")
        return [index,pages]
        break
      else:
        print("NotBefore: Seems to be good")
        do = "Nothing"
  
  if notgood == False:
    return False


# a = [1, 2, 3, 4, 5]
# b = [1, 2, 4]
# 
# print(all(i in a for i in b)) # Checks if all items are in the list
# print(any(i in a for i in b)) # Checks if any item is in the list
good = []
needfix = []
for manual in section2:
  pages = manual.split(",")
  pages = list(map(int,pages))
  print("pages:",pages)

  ret = checkbad([after,notbefore],pages)
  if ret != False:
    needfix.append(ret)

print("###\n### Working on needfix\n###")
for wrongindex,pages in needfix:
  print(wrongindex,pages)

  for index,page in enumerate(pages):
    check = copy(pages)
    check[index], check[wrongindex] = check[wrongindex], check[index]

    ret = checkbad([after,notbefore],check)
    print("tried to fix",pages,"with",check,"resulting checkbad:",ret)
    if not ret:
      good.append(check)
      break
  else:
    do = "Nothing"

print(good)


